# ============================================================
# analysis_tce.R
# TCE (Two-Component Emotion) direction-slope analysis
#
# Per-person OLS slope of Arousal ~ Change (signed), tested against zero
# via t-test and ttestBF (two-sided). Six tests per study:
# overall / acceleration / deceleration × hits / misses.
# ============================================================


# ── Helper: extract per-person slopes and test against zero ───

.slope_test <- function(data,
                         study_label,
                         condition_label,
                         direction_label,
                         change_col  = "Change",
                         arousal_col = "Arousal",
                         id_col      = "id",
                         min_trials_pp = 3,
                         min_pp        = 10) {

  # Require non-zero variance in Change within each participant
  slopes <- data |>
    dplyr::group_by(.data[[id_col]]) |>
    dplyr::group_map(function(g, key) {
      g <- tidyr::drop_na(g, dplyr::all_of(c(change_col, arousal_col)))
      if (nrow(g) < min_trials_pp) return(NULL)
      x <- g[[change_col]]
      if (stats::sd(x, na.rm = TRUE) < 1e-10) return(NULL)
      m <- stats::lm(
        stats::as.formula(paste(arousal_col, "~", change_col)),
        data = g)
      stats::coef(m)[[change_col]]
    }) |>
    purrr::compact() |>
    unlist()

  if (length(slopes) < min_pp) {
    message(sprintf("  [%s | %s | %s] Only %d participants — skipping",
                    study_label, condition_label, direction_label,
                    length(slopes)))
    return(NULL)
  }

  tt <- stats::t.test(slopes, mu = 0)

  tibble::tibble(
    study      = study_label,
    condition  = condition_label,   # "hits" or "misses"
    direction  = direction_label,   # "overall", "acceleration", "deceleration"
    n_pp       = length(slopes),
    slope_M    = mean(slopes),
    slope_SD   = stats::sd(slopes),
    t          = unname(tt$statistic),
    df         = unname(tt$parameter),
    p          = tt$p.value,
    cohens_dz  = unname(tt$statistic) / sqrt(length(slopes)),
    ci_lower   = tt$conf.int[1],
    ci_upper   = tt$conf.int[2]
  )
}


# ── Main TCE function ──────────────────────────────────────────

run_tce <- function(long_data,
                     study_label,
                     change_col  = "Change",
                     arousal_col = "Arousal",
                     id_col      = "id") {

  # Base filter: change trials only, both variables present
  base <- long_data |>
    dplyr::filter(
      Direction %in% c("Faster", "Slower"),
      !is.na(Accuracy),
      !is.na(.data[[change_col]]),
      !is.na(.data[[arousal_col]])
    )

  hits   <- dplyr::filter(base, Accuracy == 1)
  misses <- dplyr::filter(base, Accuracy == 0)
  faster_hits   <- dplyr::filter(hits,   Direction == "Faster")
  faster_misses <- dplyr::filter(misses, Direction == "Faster")
  slower_hits   <- dplyr::filter(hits,   Direction == "Slower")
  slower_misses <- dplyr::filter(misses, Direction == "Slower")

  dplyr::bind_rows(
    # Test 1: overall Change -> Arousal on hits
    .slope_test(hits,          study_label, "hits",   "overall",
                change_col, arousal_col, id_col),
    # Test 2: overall Change -> Arousal on misses
    .slope_test(misses,        study_label, "misses", "overall",
                change_col, arousal_col, id_col),
    # Test 3: acceleration -> Arousal on hits
    .slope_test(faster_hits,   study_label, "hits",   "acceleration",
                change_col, arousal_col, id_col),
    # Test 4: acceleration -> Arousal on misses
    .slope_test(faster_misses, study_label, "misses", "acceleration",
                change_col, arousal_col, id_col),
    # Test 5: deceleration -> Arousal on hits
    .slope_test(slower_hits,   study_label, "hits",   "deceleration",
                change_col, arousal_col, id_col),
    # Test 6: deceleration -> Arousal on misses
    .slope_test(slower_misses, study_label, "misses", "deceleration",
                change_col, arousal_col, id_col)
  )
}


# ── Run across studies ─────────────────────────────────────────
#
# Studies included: 1A, 2, 4, 5
# Study 1B excluded: not included in TCE analysis (different design)
# Study 3 excluded: no no-change baseline; misattribution design
#
# Note on Change variable:
#   Studies 1A, 2: Change is in % units (larger magnitude numbers)
#   Studies 4, 5:  Change is signed decimal (negative = faster)
#   Slopes are not directly comparable across studies in raw units;
#   compare direction and significance pattern, not magnitude.

message("\n========================================")
message("TCE: direction-slope analysis")
message("========================================")

tce_results <- dplyr::bind_rows(
  run_tce(dplyr::filter(s1l, Group == "TaskA"), "Study1A"),
  run_tce(s2l,             "Study2"),
  run_tce(s4l,             "Study4"),
  run_tce(s5_long_breath,  "Study5")
)

# Print summary
message("\n--- Results ---")
print(
  tce_results |>
    dplyr::mutate(
      sig = dplyr::case_when(
        p < .001 ~ "***",
        p < .01  ~ "**",
        p < .05  ~ "*",
        TRUE     ~ "ns"),
      slope_M = round(slope_M, 4),
      t       = round(t, 3),
      p       = round(p, 4),
      cohens_dz = round(cohens_dz, 3)
    ) |>
    dplyr::select(study, condition, direction,
                  n_pp, slope_M, t, p, sig, cohens_dz)
)

# Save
readr::write_csv(tce_results,
                 paste0(RESULTS_DIR, "barrett_tce_direction_slopes.csv"))
message("Saved: barrett_tce_direction_slopes.csv")


# ── Bayesian TCE: ttestBF on per-person slopes ─────────────────
#
# Bayesian parallel: ttestBF two-sided on same slopes (JZS prior r=0.707).

.slope_test_bayes <- function(data,
                               study_label,
                               condition_label,
                               direction_label,
                               change_col    = "Change",
                               arousal_col   = "Arousal",
                               id_col        = "id",
                               min_trials_pp = 3,
                               min_pp        = 10) {

  # Extract same per-person slopes as frequentist version
  slopes <- data |>
    dplyr::group_by(.data[[id_col]]) |>
    dplyr::group_map(function(g, key) {
      g <- tidyr::drop_na(g, dplyr::all_of(c(change_col, arousal_col)))
      if (nrow(g) < min_trials_pp) return(NULL)
      x <- g[[change_col]]
      if (stats::sd(x, na.rm = TRUE) < 1e-10) return(NULL)
      stats::coef(stats::lm(
        stats::as.formula(paste(arousal_col, "~", change_col)),
        data = g))[[change_col]]
    }) |>
    purrr::compact() |>
    unlist()

  if (length(slopes) < min_pp) {
    message(sprintf("  [%s | %s | %s] Only %d participants — skipping Bayes",
                    study_label, condition_label, direction_label,
                    length(slopes)))
    return(NULL)
  }

  bf_obj <- tryCatch(
    BayesFactor::ttestBF(slopes, mu = 0),
    error = function(e) {
      message(sprintf("  BF error [%s %s %s]: %s",
                      study_label, condition_label, direction_label,
                      e$message))
      NULL
    }
  )

  if (is.null(bf_obj)) return(NULL)

  bf10 <- exp(bf_obj@bayesFactor$bf)
  bf01 <- 1 / bf10

  tibble::tibble(
    study      = study_label,
    condition  = condition_label,
    direction  = direction_label,
    n_pp       = length(slopes),
    slope_M    = mean(slopes),
    BF10       = bf10,
    BF01       = bf01,
    log_BF10   = log(bf10),
    interp_hits = dplyr::case_when(
      condition_label != "hits" ~ NA_character_,
      bf10 > 100  ~ "Extreme: slope ≠ 0",
      bf10 > 10   ~ "Strong: slope ≠ 0",
      bf10 > 3    ~ "Moderate: slope ≠ 0",
      bf10 > 1    ~ "Anecdotal: slope ≠ 0",
      bf01 > 3    ~ "Moderate FOR null",
      TRUE        ~ "Inconclusive"),
    interp_miss = dplyr::case_when(
      condition_label != "misses" ~ NA_character_,
      bf01 > 100  ~ "Extreme FOR null: slope = 0",
      bf01 > 10   ~ "Strong FOR null: slope = 0",
      bf01 > 3    ~ "Moderate FOR null: slope = 0",
      bf10 > 10   ~ "Strong AGAINST null: slope ≠ 0",
      bf10 > 3    ~ "Moderate AGAINST null: slope ≠ 0",
      TRUE        ~ "Inconclusive")
  )
}


run_tce_bayes <- function(long_data,
                           study_label,
                           change_col  = "Change",
                           arousal_col = "Arousal",
                           id_col      = "id") {

  base <- long_data |>
    dplyr::filter(
      Direction %in% c("Faster", "Slower"),
      !is.na(Accuracy),
      !is.na(.data[[change_col]]),
      !is.na(.data[[arousal_col]])
    )

  hits           <- dplyr::filter(base, Accuracy == 1)
  misses         <- dplyr::filter(base, Accuracy == 0)
  faster_hits    <- dplyr::filter(hits,   Direction == "Faster")
  faster_misses  <- dplyr::filter(misses, Direction == "Faster")
  slower_hits    <- dplyr::filter(hits,   Direction == "Slower")
  slower_misses  <- dplyr::filter(misses, Direction == "Slower")

  dplyr::bind_rows(
    .slope_test_bayes(hits,          study_label, "hits",   "overall",      change_col, arousal_col, id_col),
    .slope_test_bayes(misses,        study_label, "misses", "overall",      change_col, arousal_col, id_col),
    .slope_test_bayes(faster_hits,   study_label, "hits",   "acceleration", change_col, arousal_col, id_col),
    .slope_test_bayes(faster_misses, study_label, "misses", "acceleration", change_col, arousal_col, id_col),
    .slope_test_bayes(slower_hits,   study_label, "hits",   "deceleration", change_col, arousal_col, id_col),
    .slope_test_bayes(slower_misses, study_label, "misses", "deceleration", change_col, arousal_col, id_col)
  )
}


message("\n--- Bayesian TCE ---")

tce_bayes <- dplyr::bind_rows(
  run_tce_bayes(dplyr::filter(s1l, Group == "TaskA"), "Study1A"),
  run_tce_bayes(s2l,            "Study2"),
  run_tce_bayes(s4l,            "Study4"),
  run_tce_bayes(s5_long_breath, "Study5")
)

# Print summary: hits (BF10) and misses (BF01) side by side
message("\nHits — evidence slope ≠ 0 (BF10):")
print(
  tce_bayes |>
    dplyr::filter(condition == "hits") |>
    dplyr::mutate(BF10 = round(BF10, 2), log_BF10 = round(log_BF10, 2)) |>
    dplyr::select(study, direction, n_pp, slope_M, BF10, log_BF10, interp_hits)
)

message("\nMisses — evidence FOR null (BF01):")
print(
  tce_bayes |>
    dplyr::filter(condition == "misses") |>
    dplyr::mutate(BF01 = round(BF01, 2), BF10 = round(BF10, 2)) |>
    dplyr::select(study, direction, n_pp, slope_M, BF10, BF01, interp_miss)
)

readr::write_csv(tce_bayes,
                 paste0(RESULTS_DIR, "barrett_tce_bayes.csv"))
message("Saved: barrett_tce_bayes.csv")


# ── Sensitivity checks for TCE analyses ───────────────────────
#
# Three robustness checks reported in Supplementary Materials:
#
# Check 1 — Regime: compare min 3 vs min 6 trials per participant
#   Tests whether slope estimates are stable when noisier
#   participants (fewer trials) are excluded.
#
# Check 2 — Matched magnitude: restrict to overlapping range of
#   abs(Change) between hits and misses within each direction.
#   Tests whether the hit/miss slope difference could be driven
#   by systematic magnitude differences between conditions.
#   (Note: 99-100% of trials are retained in all analyses,
#   confirming near-complete magnitude overlap.)
#
# Check 3 — Prior sensitivity: re-run Bayesian ttestBF with
#   r = 0.3, 0.5, and 0.707 (default) to confirm conclusions
#   are not dependent on the choice of prior width.


# ── Check 1: Regime ───────────────────────────────────────────

message("\n--- Sensitivity Check 1: Regime (min 3 vs min 6 trials) ---")

.run_tce_regime <- function(long_data, study_label,
                              min_trials_pp,
                              change_col  = "Change",
                              arousal_col = "Arousal",
                              id_col      = "id") {

  base <- long_data |>
    dplyr::filter(Direction %in% c("Faster","Slower"),
                  !is.na(Accuracy),
                  !is.na(.data[[change_col]]),
                  !is.na(.data[[arousal_col]]))

  purrr::map_dfr(
    list(
      list(acc = 1, cond = "hits"),
      list(acc = 0, cond = "misses")
    ),
    function(a) {
      sub <- dplyr::filter(base, Accuracy == a$acc)
      purrr::map_dfr(
        list(
          list(dir = NULL,     label = "overall"),
          list(dir = "Faster", label = "acceleration"),
          list(dir = "Slower", label = "deceleration")
        ),
        function(d) {
          dd <- if (!is.null(d$dir))
            dplyr::filter(sub, Direction == d$dir) else sub
          result <- .slope_test(dd, study_label, a$cond, d$label,
                                change_col, arousal_col, id_col,
                                min_trials_pp = min_trials_pp)
          if (!is.null(result))
            dplyr::mutate(result, min_trials = min_trials_pp)
          else NULL
        }
      )
    }
  )
}

regime_results <- purrr::map_dfr(
  list(
    list(data = dplyr::filter(s1l, Group == "TaskA"), label = "Study1A"),
    list(data = s2l,            label = "Study2"),
    list(data = s4l,            label = "Study4"),
    list(data = s5_long_breath, label = "Study5")
  ),
  function(s) {
    dplyr::bind_rows(
      .run_tce_regime(s$data, s$label, min_trials_pp = 3),
      .run_tce_regime(s$data, s$label, min_trials_pp = 6)
    )
  }
)

# Flag any significance reversals
reversals <- regime_results |>
  dplyr::group_by(study, condition, direction) |>
  dplyr::summarise(
    p_min3  = p[min_trials == 3],
    p_min6  = p[min_trials == 6],
    sig_min3 = p[min_trials == 3] < .05,
    sig_min6 = p[min_trials == 6] < .05,
    reversal = sig_min3 != sig_min6,
    .groups = "drop"
  ) |>
  dplyr::filter(reversal)

if (nrow(reversals) == 0) {
  message("  No significance reversals — conclusions stable across regimes")
} else {
  message("  Reversals detected:")
  print(reversals)
}

readr::write_csv(regime_results,
                 paste0(RESULTS_DIR, "tce_sensitivity_regime.csv"))
message("Saved: tce_sensitivity_regime.csv")


# ── Check 2: Matched magnitude ────────────────────────────────

message("\n--- Sensitivity Check 2: Matched magnitude ---")

.run_tce_matched <- function(long_data, study_label,
                               change_col  = "Change",
                               arousal_col = "Arousal",
                               id_col      = "id") {

  base <- long_data |>
    dplyr::filter(Direction %in% c("Faster","Slower"),
                  !is.na(Accuracy),
                  !is.na(.data[[change_col]]),
                  !is.na(.data[[arousal_col]])) |>
    dplyr::mutate(abs_change = abs(.data[[change_col]]))

  purrr::map_dfr(
    list(
      list(dir = "Faster", label = "acceleration"),
      list(dir = "Slower", label = "deceleration")
    ),
    function(d) {
      dd <- dplyr::filter(base, Direction == d$dir)

      hits_range   <- range(dd$abs_change[dd$Accuracy == 1], na.rm = TRUE)
      misses_range <- range(dd$abs_change[dd$Accuracy == 0], na.rm = TRUE)
      lo <- max(hits_range[1], misses_range[1])
      hi <- min(hits_range[2], misses_range[2])

      dd_matched <- dplyr::filter(dd, abs_change >= lo, abs_change <= hi)
      pct_retained <- nrow(dd_matched) / nrow(dd) * 100

      purrr::map_dfr(
        list(list(acc = 1, cond = "hits"), list(acc = 0, cond = "misses")),
        function(a) {
          sub <- dplyr::filter(dd_matched, Accuracy == a$acc)
          result <- .slope_test(sub, study_label, a$cond, d$label,
                                change_col, arousal_col, id_col)
          if (!is.null(result))
            dplyr::mutate(result,
                          range_lo = lo, range_hi = hi,
                          pct_retained = round(pct_retained, 1))
          else NULL
        }
      )
    }
  )
}

matched_results <- purrr::map_dfr(
  list(
    list(data = dplyr::filter(s1l, Group == "TaskA"), label = "Study1A"),
    list(data = s2l,            label = "Study2"),
    list(data = s4l,            label = "Study4"),
    list(data = s5_long_breath, label = "Study5")
  ),
  function(s) .run_tce_matched(s$data, s$label)
)

message("  Retention rates (should be ~99-100%):")
matched_results |>
  dplyr::distinct(study, direction, pct_retained) |>
  print()

readr::write_csv(matched_results,
                 paste0(RESULTS_DIR, "tce_sensitivity_matched.csv"))
message("Saved: tce_sensitivity_matched.csv")


# ── Check 3: Prior sensitivity ────────────────────────────────

message("\n--- Sensitivity Check 3: Bayesian prior sensitivity ---")
message("  Re-running ttestBF with r = 0.3, 0.5, 0.707 on key tests")
message("  (deceleration misses and acceleration hits/misses)")

.slope_test_bayes_r <- function(data, study_label,
                                  condition_label, direction_label,
                                  r_scale,
                                  change_col    = "Change",
                                  arousal_col   = "Arousal",
                                  id_col        = "id",
                                  min_trials_pp = 3,
                                  min_pp        = 10) {
  slopes <- data |>
    dplyr::group_by(.data[[id_col]]) |>
    dplyr::group_map(function(g, key) {
      g <- tidyr::drop_na(g, dplyr::all_of(c(change_col, arousal_col)))
      if (nrow(g) < min_trials_pp) return(NULL)
      x <- g[[change_col]]
      if (stats::sd(x, na.rm = TRUE) < 1e-10) return(NULL)
      stats::coef(stats::lm(
        stats::as.formula(paste(arousal_col, "~", change_col)),
        data = g))[[change_col]]
    }) |>
    purrr::compact() |>
    unlist()

  if (length(slopes) < min_pp) return(NULL)

  bf_obj <- tryCatch(
    BayesFactor::ttestBF(slopes, mu = 0, rscale = r_scale),
    error = function(e) NULL
  )
  if (is.null(bf_obj)) return(NULL)

  bf10 <- exp(bf_obj@bayesFactor$bf)
  tibble::tibble(
    study      = study_label,
    condition  = condition_label,
    direction  = direction_label,
    r_scale    = r_scale,
    n_pp       = length(slopes),
    slope_M    = mean(slopes),
    BF10       = bf10,
    BF01       = 1 / bf10,
    log_BF10   = log(bf10)
  )
}

# Key tests only (deceleration misses, acceleration hits/misses)
key_specs <- list(
  list(acc = 0, cond = "misses", dir = "Slower", label = "deceleration"),
  list(acc = 1, cond = "hits",   dir = "Faster", label = "acceleration"),
  list(acc = 0, cond = "misses", dir = "Faster", label = "acceleration")
)

prior_results <- purrr::map_dfr(
  list(
    list(data = dplyr::filter(s1l, Group == "TaskA"), label = "Study1A"),
    list(data = s2l,            label = "Study2"),
    list(data = s4l,            label = "Study4"),
    list(data = s5_long_breath, label = "Study5")
  ),
  function(s) {
    purrr::map_dfr(key_specs, function(spec) {
      sub <- dplyr::filter(s$data,
                            Accuracy  == spec$acc,
                            Direction == spec$dir)
      purrr::map_dfr(c(0.3, 0.5, 0.707), function(r) {
        .slope_test_bayes_r(sub, s$label, spec$cond, spec$label,
                             r_scale = r)
      })
    })
  }
)

# Print pivot for easy reading
cat("\nBF10 across prior widths (key tests):\n")
prior_wide <- prior_results |>
  dplyr::mutate(r_label = paste0("BF10_r", r_scale)) |>
  dplyr::select(study, condition, direction, r_label, BF10) |>
  tidyr::pivot_wider(names_from = r_label, values_from = BF10)
print(prior_wide)

readr::write_csv(prior_results,
                 paste0(RESULTS_DIR, "tce_sensitivity_prior.csv"))
message("Saved: tce_sensitivity_prior.csv")


# ── Consolidated supplement table ─────────────────────────────

tce_sensitivity_supplement <- dplyr::bind_rows(
  regime_results  |> dplyr::mutate(check = "regime"),
  matched_results |> dplyr::mutate(check = "matched_magnitude",
                                    min_trials = NA_integer_),
  prior_results   |> dplyr::mutate(check = "prior_sensitivity",
                                    min_trials = NA_integer_,
                                    cohens_dz = NA_real_,
                                    t = NA_real_, df = NA_real_,
                                    p = NA_real_,
                                    ci_lower = NA_real_, ci_upper = NA_real_)
)

readr::write_csv(tce_sensitivity_supplement,
                 paste0(RESULTS_DIR, "tce_sensitivity_consolidated.csv"))
message("Saved: tce_sensitivity_consolidated.csv")

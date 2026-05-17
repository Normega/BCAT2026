# ============================================================
# analysis_tce.R
# TCE Arousal-Change Analysis: Model Progression and Regime Sensitivity
#
# Tests whether breathing rate change predicts subjective arousal
# separately for detected (hit) and missed trials. Direction
# decomposition (acceleration vs. deceleration) is not performed
# here -- the pre-registered direction effect on DETECTION ACCURACY
# is reported in the threshold analyses; differential direction
# effects on AROUSAL are exploratory and not replicated across
# samples.
#
# Approach: per-person OLS coefficients from model progression
#   M1: Arousal ~ Change           (linear)
#   M2: Arousal ~ Change + Change2 (linear + quadratic)
# Coefficients tested against zero via t-test (frequentist) and
# ttestBF (Bayesian, JZS r = 0.707).
#
# Sensitivity checks:
#   Regime        : min 3 vs min 6 trials per participant
#   Matched mag.  : restrict to overlapping Change range (hits/misses)
#   Prior sens.   : Bayesian re-run with r = 0.3, 0.5, 0.707
#
# Studies: 1A, 2, 4, 5
# Study 1B excluded: different design (limits method)
# Study 3 excluded: fixed magnitudes, no no-change baseline
#
# Change variable units differ by study:
#   Studies 1A, 2 : % of baseline rate (larger numbers)
#   Studies 4, 5  : signed decimal (negative = faster)
# Compare direction and significance, not raw magnitude.
# ============================================================

# ── Per-person model extraction helper ────────────────────────
#
# Fits M1 (linear) and M2 (linear + quadratic) per person,
# returns tibble of coefficients (β_change, β_change2) with
# participant count. Returns NULL if fewer than min_pp participants
# contribute valid estimates.

.extract_pp_coefs <- function(data,
                               change_col    = "Change",
                               arousal_col   = "Arousal",
                               id_col        = "id",
                               min_trials_pp = 3) {

  data |>
    dplyr::group_by(.data[[id_col]]) |>
    dplyr::group_map(function(g, key) {
      g <- tidyr::drop_na(g, dplyr::all_of(c(change_col, arousal_col)))
      if (nrow(g) < min_trials_pp) return(NULL)
      x <- g[[change_col]]
      if (stats::sd(x, na.rm = TRUE) < 1e-10) return(NULL)

      # M1: linear only
      m1 <- stats::lm(
        stats::as.formula(paste(arousal_col, "~", change_col)),
        data = g)

      # M2: linear + quadratic
      g$Change2 <- x^2
      m2 <- stats::lm(
        stats::as.formula(paste(arousal_col, "~ Change +  Change2")),
        data = g)

      tibble::tibble(
        b_change_m1  = stats::coef(m1)[[change_col]],
        b_change_m2  = stats::coef(m2)[["Change"]],
        b_change2_m2 = stats::coef(m2)[["Change2"]]
      )
    }) |>
    purrr::compact() |>
    dplyr::bind_rows()
}


# ── Frequentist slope test ─────────────────────────────────────
#
# Takes a vector of per-person coefficients, tests against zero.

.test_slopes <- function(slopes, coef_name) {
  slopes <- slopes[is.finite(slopes)] 
  if (length(slopes) < 5) return(NULL)
  tt <- stats::t.test(slopes, mu = 0)
  tibble::tibble(
    coef      = coef_name,
    n_pp      = length(slopes),
    M         = mean(slopes),
    SD        = stats::sd(slopes),
    t         = unname(tt$statistic),
    df        = unname(tt$parameter),
    p         = tt$p.value,
    cohens_dz = unname(tt$statistic) / sqrt(length(slopes)),
    ci_lower  = tt$conf.int[1],
    ci_upper  = tt$conf.int[2]
  )
}


# ── Main TCE function ──────────────────────────────────────────

run_tce <- function(long_data,
                     study_label,
                     change_col    = "Change",
                     arousal_col   = "Arousal",
                     id_col        = "id",
                     min_trials_pp = 3) {

  base <- long_data |>
    dplyr::filter(
      Direction %in% c("Faster", "Slower"),
      !is.na(Accuracy),
      !is.na(.data[[change_col]]),
      !is.na(.data[[arousal_col]])
    )

  hits   <- dplyr::filter(base, Accuracy == 1)
  misses <- dplyr::filter(base, Accuracy == 0)

  purrr::map_dfr(
    list(list(data = hits, cond = "hits"),
         list(data = misses, cond = "misses")),
    function(a) {
      coefs <- .extract_pp_coefs(a$data, change_col, arousal_col,
                                  id_col, min_trials_pp)
      if (nrow(coefs) < 5) {
        message(sprintf("  [%s | %s] Too few participants — skipping",
                        study_label, a$cond))
        return(NULL)
      }
      dplyr::bind_rows(
        .test_slopes(coefs$b_change_m1,  "b_change_M1"),
        .test_slopes(coefs$b_change_m2,  "b_change_M2"),
        .test_slopes(coefs$b_change2_m2, "b_change2_M2")
      ) |>
        dplyr::mutate(
          study     = study_label,
          condition = a$cond,
          min_trials = min_trials_pp,
          .before = 1
        )
    }
  )
}


# ── Bayesian t-test on per-person slopes ──────────────────────

.test_slopes_bayes <- function(slopes, coef_name,
                                study_label, condition_label,
                                r_scale = 0.707) {
  slopes <- slopes[is.finite(slopes)] 
  if (length(slopes) < 5) return(NULL)
  bf_obj <- tryCatch(
    BayesFactor::ttestBF(slopes, mu = 0, rscale = r_scale),
    error = function(e) {
      message(sprintf("  BF error [%s | %s | %s]: %s",
                      study_label, condition_label, coef_name, e$message))
      NULL
    }
  )
  if (is.null(bf_obj)) return(NULL)
  bf10 <- exp(bf_obj@bayesFactor$bf)
  bf01 <- 1 / bf10
  tibble::tibble(
    study     = study_label,
    condition = condition_label,
    coef      = coef_name,
    r_scale   = r_scale,
    n_pp      = length(slopes),
    M         = mean(slopes),
    BF10      = bf10,
    BF01      = bf01,
    log_BF10  = log(bf10),
    interp    = dplyr::case_when(
      bf10 > 100 ~ "Extreme evidence: slope ≠ 0",
      bf10 > 10  ~ "Strong evidence: slope ≠ 0",
      bf10 > 3   ~ "Moderate evidence: slope ≠ 0",
      bf10 > 1   ~ "Anecdotal: slope ≠ 0",
      bf01 > 100 ~ "Extreme evidence FOR null",
      bf01 > 10  ~ "Strong evidence FOR null",
      bf01 > 3   ~ "Moderate evidence FOR null",
      TRUE       ~ "Inconclusive"
    )
  )
}

run_tce_bayes <- function(long_data, study_label,
                            change_col    = "Change",
                            arousal_col   = "Arousal",
                            id_col        = "id",
                            min_trials_pp = 3,
                            r_scale       = 0.707) {

  base <- long_data |>
    dplyr::filter(
      Direction %in% c("Faster", "Slower"),
      !is.na(Accuracy),
      !is.na(.data[[change_col]]),
      !is.na(.data[[arousal_col]])
    )

  purrr::map_dfr(
    list(list(data = dplyr::filter(base, Accuracy == 1), cond = "hits"),
         list(data = dplyr::filter(base, Accuracy == 0), cond = "misses")),
    function(a) {
      coefs <- .extract_pp_coefs(a$data, change_col, arousal_col,
                                  id_col, min_trials_pp)
      if (nrow(coefs) < 5) return(NULL)
      dplyr::bind_rows(
        .test_slopes_bayes(coefs$b_change_m1,  "b_change_M1",
                            study_label, a$cond, r_scale),
        .test_slopes_bayes(coefs$b_change_m2,  "b_change_M2",
                            study_label, a$cond, r_scale),
        .test_slopes_bayes(coefs$b_change2_m2, "b_change2_M2",
                            study_label, a$cond, r_scale)
      )
    }
  )
}


# ── Run primary analyses ───────────────────────────────────────

message("\n========================================")
message("TCE: Model progression (hits vs. misses)")
message("========================================")

studies <- list(
  list(data = dplyr::filter(s1l, Group == "TaskA"), label = "Study1A"),
  list(data = s2l,            label = "Study2"),
  list(data = s4l,            label = "Study4"),
  list(data = s5_long_breath, label = "Study5")
)

# Primary frequentist results (min 3 trials)
tce_primary <- purrr::map_dfr(studies, function(s) {
  run_tce(s$data, s$label, min_trials_pp = 3)
})

message("\n--- Frequentist results (min 3 trials) ---")
print(
  tce_primary |>
    dplyr::mutate(
      sig = dplyr::case_when(
        p < .001 ~ "***", p < .01 ~ "**", p < .05 ~ "*", TRUE ~ "ns"),
      M = round(M, 4), t = round(t, 3), p = round(p, 4),
      cohens_dz = round(cohens_dz, 3)
    ) |>
    dplyr::select(study, condition, coef, n_pp, M, t, p, sig, cohens_dz)
)

# Primary Bayesian results
tce_bayes <- purrr::map_dfr(studies, function(s) {
  run_tce_bayes(s$data, s$label)
})

message("\n--- Bayesian results (r = 0.707) ---")
message("Hits (BF10 — evidence slope ≠ 0):")
print(
  tce_bayes |>
    dplyr::filter(condition == "hits") |>
    dplyr::mutate(BF10 = round(BF10, 2), log_BF10 = round(log_BF10, 2)) |>
    dplyr::select(study, coef, n_pp, M, BF10, log_BF10, interp)
)
message("Misses (BF01 — evidence FOR null):")
print(
  tce_bayes |>
    dplyr::filter(condition == "misses") |>
    dplyr::mutate(BF01 = round(BF01, 2), BF10 = round(BF10, 2)) |>
    dplyr::select(study, coef, n_pp, M, BF10, BF01, interp)
)

readr::write_csv(tce_primary,
                 paste0(RESULTS_DIR, "tce_primary_results.csv"))
readr::write_csv(tce_bayes,
                 paste0(RESULTS_DIR, "barrett_tce_bayes.csv"))
message("Saved: tce_primary_results.csv")
message("Saved: barrett_tce_bayes.csv")


# ── Sensitivity Check 1: Regime ───────────────────────────────
#
# Repeat with min 3 and min 6 trials per participant.
# Tests whether conclusions depend on including noisier
# participants who contribute fewer trials.

message("\n--- Sensitivity Check 1: Regime (min 3 vs min 6) ---")

regime_results <- purrr::map_dfr(studies, function(s) {
  dplyr::bind_rows(
    run_tce(s$data, s$label, min_trials_pp = 3),
    run_tce(s$data, s$label, min_trials_pp = 6)
  )
})

# Flag significance reversals
reversals <- regime_results |>
  dplyr::group_by(study, condition, coef) |>
  dplyr::summarise(
    sig_min3 = p[min_trials == 3] < .05,
    sig_min6 = p[min_trials == 6] < .05,
    reversal = sig_min3 != sig_min6,
    .groups = "drop"
  ) |>
  dplyr::filter(reversal)

if (nrow(reversals) == 0) {
  message("  No significance reversals -- conclusions stable across regimes")
} else {
  message("  Reversals detected:")
  print(reversals)
}

readr::write_csv(regime_results,
                 paste0(RESULTS_DIR, "tce_sensitivity_regime.csv"))
message("Saved: tce_sensitivity_regime.csv")


# ── Sensitivity Check 2: Matched magnitude ────────────────────
#
# Restrict to overlapping range of |Change| between hits and misses.
# Computed overall (not by direction): the hit and miss Change
# distributions are compared collapsed across direction to confirm
# near-complete overlap.

message("\n--- Sensitivity Check 2: Matched magnitude ---")

.run_tce_matched <- function(long_data, study_label,
                               change_col  = "Change",
                               arousal_col = "Arousal",
                               id_col      = "id") {

  base <- long_data |>
    dplyr::filter(
      Direction %in% c("Faster", "Slower"),
      !is.na(Accuracy),
      !is.na(.data[[change_col]]),
      !is.na(.data[[arousal_col]])
    ) |>
    dplyr::mutate(abs_change = abs(.data[[change_col]]))

  hits_range   <- range(base$abs_change[base$Accuracy == 1], na.rm = TRUE)
  misses_range <- range(base$abs_change[base$Accuracy == 0], na.rm = TRUE)
  lo <- max(hits_range[1], misses_range[1])
  hi <- min(hits_range[2], misses_range[2])

  matched  <- dplyr::filter(base, abs_change >= lo, abs_change <= hi)
  pct_ret  <- round(nrow(matched) / nrow(base) * 100, 1)
  message(sprintf("  [%s] Matched range: [%.3f, %.3f], %.1f%% retained",
                  study_label, lo, hi, pct_ret))

  purrr::map_dfr(
    list(list(acc = 1, cond = "hits"),
         list(acc = 0, cond = "misses")),
    function(a) {
      sub   <- dplyr::filter(matched, Accuracy == a$acc)
      coefs <- .extract_pp_coefs(sub, change_col, arousal_col, id_col, 3)
      if (nrow(coefs) < 5) return(NULL)
      dplyr::bind_rows(
        .test_slopes(coefs$b_change_m1,  "b_change_M1"),
        .test_slopes(coefs$b_change_m2,  "b_change_M2"),
        .test_slopes(coefs$b_change2_m2, "b_change2_M2")
      ) |>
        dplyr::mutate(
          study        = study_label,
          condition    = a$cond,
          range_lo     = lo,
          range_hi     = hi,
          pct_retained = pct_ret,
          .before = 1
        )
    }
  )
}

matched_results <- purrr::map_dfr(studies, function(s) {
  .run_tce_matched(s$data, s$label)
})

readr::write_csv(matched_results,
                 paste0(RESULTS_DIR, "tce_sensitivity_matched.csv"))
message("Saved: tce_sensitivity_matched.csv")


# ── Sensitivity Check 3: Bayesian prior sensitivity ───────────
#
# Re-run ttestBF on overall hit and miss slopes (M1 and M2 linear
# terms) with r = 0.3, 0.5, 0.707 to confirm prior robustness.

message("\n--- Sensitivity Check 3: Prior sensitivity ---")

prior_results <- purrr::map_dfr(studies, function(s) {
  base <- s$data |>
    dplyr::filter(
      Direction %in% c("Faster", "Slower"),
      !is.na(Accuracy), !is.na(Change), !is.na(Arousal)
    )

  purrr::map_dfr(
    list(list(data = dplyr::filter(base, Accuracy == 1), cond = "hits"),
         list(data = dplyr::filter(base, Accuracy == 0), cond = "misses")),
    function(a) {
      coefs <- .extract_pp_coefs(a$data, min_trials_pp = 3)
      if (nrow(coefs) < 5) return(NULL)
      purrr::map_dfr(c(0.3, 0.5, 0.707), function(r) {
        dplyr::bind_rows(
          .test_slopes_bayes(coefs$b_change_m1,  "b_change_M1",
                              s$label, a$cond, r),
          .test_slopes_bayes(coefs$b_change2_m2, "b_change2_M2",
                              s$label, a$cond, r)
        )
      })
    }
  )
})

cat("\nBF10 across prior widths (hits b_change_M1):\n")
prior_results |>
  dplyr::filter(condition == "hits", coef == "b_change_M1") |>
  dplyr::mutate(BF10 = round(BF10, 2)) |>
  dplyr::select(study, r_scale, n_pp, BF10, interp) |>
  print()

cat("\nBF01 across prior widths (misses b_change_M1):\n")
prior_results |>
  dplyr::filter(condition == "misses", coef == "b_change_M1") |>
  dplyr::mutate(BF01 = round(BF01, 2)) |>
  dplyr::select(study, r_scale, n_pp, BF01, interp) |>
  print()

readr::write_csv(prior_results,
                 paste0(RESULTS_DIR, "tce_sensitivity_prior.csv"))
message("Saved: tce_sensitivity_prior.csv")


# ── Consolidated supplement table ─────────────────────────────

tce_consolidated <- dplyr::bind_rows(
  regime_results  |>
    dplyr::mutate(check = "regime"),
  matched_results |>
    dplyr::mutate(check = "matched_magnitude", min_trials = NA_integer_),
  prior_results   |>
    dplyr::mutate(check = "prior_sensitivity",
                  min_trials = NA_integer_,
                  cohens_dz  = NA_real_,
                  t = NA_real_, df = NA_real_, p = NA_real_,
                  ci_lower = NA_real_, ci_upper = NA_real_)
)

readr::write_csv(tce_consolidated,
                 paste0(RESULTS_DIR, "tce_sensitivity_consolidated.csv"))
message("Saved: tce_sensitivity_consolidated.csv")

message("\nanalysis_tce.R complete.")

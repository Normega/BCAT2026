# Test Block Arousal and Confidence Analysis
# Examines whether salience manipulation affects arousal and confidence in test blocks
# (Studies 4 and 5), complementing existing accuracy analyses (H5)
#
# Prediction: low-salience trials (tested at high-salience threshold) produce
# lower detection rates, and thereby lower arousal and confidence.
# Key test: whether salience effect on arousal/confidence is mediated by detection.

# Set Up ---------
## Load libraries ---------
packages <- c(
  "tidyverse",
  "lme4",
  "lmerTest",
  "ggeffects",
  "patchwork",
  "mediation",
  "BayesFactor",
  "brms",
  "tidybayes",
  "broom.mixed"
)
new_packages <- packages[!sapply(packages, requireNamespace, quietly = TRUE)]
if (length(new_packages)) install.packages(new_packages)
options(readr.show_col_types = FALSE)
for (thispack in packages) {
  library(thispack, character.only = TRUE, quietly = TRUE, verbose = FALSE)
}

# Paths ---------
DATA_DIR    <- file.path(MAIN_DIR, "Data")
RESULTS_DIR <- file.path(MAIN_DIR, "Results")
dir.create(RESULTS_DIR, showWarnings = FALSE, recursive = TRUE)

# ============================================================
# 1. LOAD DATA
# ============================================================
# Expects trial-level data files for Studies 4 and 5.
# Required columns (adapt names to match your actual files):
#   id          : participant identifier
#   study       : "S4" or "S5"
#   block_type  : "staircase" | "test"  (filter to "test" below)
#   salience    : "high" | "low"
#   accuracy    : 1 = correct 3AFC, 0 = incorrect (hit/miss proxy)
#   arousal     : trial-level arousal rating (z-scored within participant)
#   confidence  : trial-level confidence rating
#   change      : signed breathing rate change magnitude
#   direction   : "faster" | "slower"

s4 <- readr::read_csv(file.path(DATA_DIR, "study4_trials.csv"))
s5 <- readr::read_csv(file.path(DATA_DIR, "study5_trials.csv"))

trials_all <- dplyr::bind_rows(
  dplyr::mutate(s4, study = "S4"),
  dplyr::mutate(s5, study = "S5")
)

# ============================================================
# 2. FILTER TO TEST BLOCK TRIALS
# ============================================================
# Exclude no-change trials (change == 0); keep only test block.
test <- trials_all |>
  dplyr::filter(block_type == "test", change != 0) |>
  dplyr::mutate(
    salience_f  = factor(salience, levels = c("high", "low")),
    accuracy_f  = factor(accuracy, levels = c(0, 1), labels = c("miss", "hit")),
    abs_change  = abs(change),
    study_f     = factor(study)
  )

# Z-score arousal and confidence within participant x study
test <- test |>
  dplyr::group_by(id, study) |>
  dplyr::mutate(
    arousal_z    = scale(arousal)[, 1],
    confidence_z = scale(confidence)[, 1]
  ) |>
  dplyr::ungroup()

cat("Test block trial counts by study and salience:\n")
test |>
  dplyr::count(study, salience_f) |>
  print()

# ============================================================
# 3. ANALYSIS 1: MARGINAL SALIENCE EFFECT ON AROUSAL & CONFIDENCE
# ============================================================
# Does salience condition alone predict arousal and confidence?
# Prediction: low salience -> lower arousal and confidence.
# Control for abs_change (constant across salience by design, but verify)
# and direction.

## 3a. Arousal
m_arousal_sal <- lmerTest::lmer(
  arousal_z ~ salience_f + abs_change + direction + study_f +
    (1 | id),
  data = test,
  REML = FALSE
)
summary(m_arousal_sal)

## 3b. Confidence
m_conf_sal <- lmerTest::lmer(
  confidence_z ~ salience_f + abs_change + direction + study_f +
    (1 | id),
  data = test,
  REML = FALSE
)
summary(m_conf_sal)

## Effect sizes (partial r)
partial_r <- function(model, term) {
  tt <- summary(model)$coefficients
  t_val <- tt[term, "t value"]
  df    <- tt[term, "df"]
  r     <- t_val / sqrt(t_val^2 + df)
  ci_lo <- tanh(atanh(r) - 1.96 / sqrt(df - 3))
  ci_hi <- tanh(atanh(r) + 1.96 / sqrt(df - 3))
  tibble::tibble(term = term, partial_r = round(r, 3),
                 ci_lo = round(ci_lo, 3), ci_hi = round(ci_hi, 3))
}

marginal_effects <- dplyr::bind_rows(
  partial_r(m_arousal_sal,  "salience_flow") |> dplyr::mutate(outcome = "arousal"),
  partial_r(m_conf_sal,     "salience_flow") |> dplyr::mutate(outcome = "confidence")
)
print(marginal_effects)

# ============================================================
# 4. ANALYSIS 2: SALIENCE EFFECT CONDITIONAL ON HIT/MISS
# ============================================================
# Does salience still predict arousal after controlling for detection status?
# If awareness-gating is the full story: salience_f should drop out once
# accuracy_f is included (no direct path from salience to arousal).

## 4a. Arousal: full model with hit/miss
m_arousal_full <- lmerTest::lmer(
  arousal_z ~ salience_f * accuracy_f + abs_change + direction + study_f +
    (1 | id),
  data = test,
  REML = FALSE
)
summary(m_arousal_full)

## 4b. Confidence: full model
m_conf_full <- lmerTest::lmer(
  confidence_z ~ salience_f * accuracy_f + abs_change + direction + study_f +
    (1 | id),
  data = test,
  REML = FALSE
)
summary(m_conf_full)

## Likelihood ratio test: does adding accuracy improve over salience-only?
lrt_arousal <- anova(m_arousal_sal, m_arousal_full)
lrt_conf    <- anova(m_conf_sal,    m_conf_full)
cat("\nLRT arousal (salience-only vs salience+accuracy):\n"); print(lrt_arousal)
cat("\nLRT confidence (salience-only vs salience+accuracy):\n"); print(lrt_conf)

# ============================================================
# 5. ANALYSIS 3: MEDIATION -- SALIENCE -> DETECTION -> AROUSAL
# ============================================================
# Formal mediation: salience affects arousal via detection accuracy.
# Uses person-level summaries for mediation package.
# Prediction: indirect effect significant; direct effect near-zero.

person_test <- test |>
  dplyr::group_by(id, study, salience_f) |>
  dplyr::summarise(
    mean_arousal    = mean(arousal_z,    na.rm = TRUE),
    mean_confidence = mean(confidence_z, na.rm = TRUE),
    mean_accuracy   = mean(accuracy,     na.rm = TRUE),
    n_trials        = dplyr::n(),
    .groups = "drop"
  ) |>
  dplyr::mutate(salience_num = ifelse(salience_f == "high", 1, 0))

# Mediator model: salience -> detection accuracy
med_model <- lm(mean_accuracy ~ salience_num, data = person_test)

# Outcome model: salience + accuracy -> arousal
out_model <- lm(mean_arousal ~ salience_num + mean_accuracy, data = person_test)

med_result <- mediation::mediate(
  med_model, out_model,
  treat = "salience_num", mediator = "mean_accuracy",
  boot = TRUE, sims = 1000
)
summary(med_result)

# Repeat for confidence as outcome
out_conf_model <- lm(mean_confidence ~ salience_num + mean_accuracy, data = person_test)
med_conf_result <- mediation::mediate(
  med_model, out_conf_model,
  treat = "salience_num", mediator = "mean_accuracy",
  boot = TRUE, sims = 1000
)
summary(med_conf_result)

# ============================================================
# 6. BAYESIAN NULL TEST: DIRECT SALIENCE EFFECT AFTER CONDITIONING
# ============================================================
# After conditioning on hit/miss, does salience retain a direct effect?
# BF01 > 3 supports the awareness-gating account (no direct path).

# Person-level: high vs low salience arousal residualized for accuracy
person_wide <- person_test |>
  dplyr::select(id, study, salience_f, mean_arousal, mean_accuracy) |>
  tidyr::pivot_wider(
    names_from  = salience_f,
    values_from = c(mean_arousal, mean_accuracy)
  ) |>
  dplyr::mutate(
    arousal_diff  = mean_arousal_high  - mean_arousal_low,
    accuracy_diff = mean_accuracy_high - mean_accuracy_low
  )

# Residualize arousal difference on accuracy difference
resid_model  <- lm(arousal_diff ~ accuracy_diff, data = person_wide)
arousal_resid <- residuals(resid_model)

bf_direct <- BayesFactor::ttestBF(arousal_resid)
cat("\nBF10 for residual salience effect on arousal (after controlling accuracy):\n")
print(bf_direct)
cat("BF01 (null):", round(1 / exp(bf_direct@bayesFactor$bf), 2), "\n")

# ============================================================
# 7. BRMS: MULTILEVEL MEDIATION (TRIAL-LEVEL)
# ============================================================
# Proper trial-level multilevel mediation using brms.
# Advantage over Section 5: preserves within-person trial variance
# rather than collapsing to person-level means.
#
# Two-equation model:
#   M model: accuracy ~ salience + controls + (1 | id)
#   Y model: arousal  ~ salience + accuracy + controls + (1 | id)
#
# Indirect effect = b_sal_on_accuracy * b_accuracy_on_arousal
# Direct effect   = b_sal_on_arousal (after conditioning on accuracy)
# Prediction: large indirect, near-zero direct.

# Numeric coding for brms (required for indirect effect computation)
test_b <- test |>
  dplyr::mutate(
    salience_num  = ifelse(salience_f == "high", 1, 0),
    accuracy_num  = as.numeric(accuracy),          # 0/1
    study_num     = as.numeric(study_f) - 1        # 0/1 dummy
  )

# Weakly informative priors consistent with z-scored outcomes
bpriors <- c(
  brms::prior(normal(0, 1),   class = "b"),
  brms::prior(normal(0, 1),   class = "Intercept"),
  brms::prior(exponential(1), class = "sd"),
  brms::prior(exponential(1), class = "sigma")
)

## 7a. Mediator model: salience -> accuracy (logistic; accuracy is 0/1)
bm_med <- brms::brm(
  accuracy_num ~ salience_num + abs_change + study_num + (1 | id),
  data   = test_b,
  family = brms::bernoulli(link = "logit"),
  prior  = bpriors[bpriors$class != "sigma", ],   # no sigma for bernoulli
  chains = 4, iter = 2000, warmup = 1000,
  cores  = 4, seed = 42,
  file   = file.path(RESULTS_DIR, "brms_mediator_model")
)
summary(bm_med)

## 7b. Outcome model: salience + accuracy -> arousal
bm_out_arousal <- brms::brm(
  arousal_z ~ salience_num + accuracy_num + abs_change + study_num + (1 | id),
  data   = test_b,
  family = brms::gaussian(),
  prior  = bpriors,
  chains = 4, iter = 2000, warmup = 1000,
  cores  = 4, seed = 42,
  file   = file.path(RESULTS_DIR, "brms_outcome_arousal")
)
summary(bm_out_arousal)

## 7c. Outcome model: salience + accuracy -> confidence
bm_out_conf <- brms::brm(
  confidence_z ~ salience_num + accuracy_num + abs_change + study_num + (1 | id),
  data   = test_b,
  family = brms::gaussian(),
  prior  = bpriors,
  chains = 4, iter = 2000, warmup = 1000,
  cores  = 4, seed = 42,
  file   = file.path(RESULTS_DIR, "brms_outcome_confidence")
)
summary(bm_out_conf)

## 7d. Compute indirect effects from posterior draws
# Extract posterior samples for key coefficients
draws_med    <- tidybayes::spread_draws(bm_med,        b_salience_num)
draws_arousal <- tidybayes::spread_draws(bm_out_arousal, b_salience_num, b_accuracy_num)
draws_conf    <- tidybayes::spread_draws(bm_out_conf,    b_salience_num, b_accuracy_num)

# Rename to avoid collision when joining
draws_med <- draws_med |>
  dplyr::rename(a_path = b_salience_num)   # salience -> accuracy (log-odds scale)

# Note: a_path is on log-odds scale; for a linear approximation of the
# indirect effect on the arousal scale, multiply by b_accuracy (linear).
# For a fully probability-scale indirect effect, use marginal effects instead.
# Here we report both the linear approximation and flag the scale caveat.

indirect_arousal <- draws_med |>
  dplyr::bind_cols(
    draws_arousal |>
      dplyr::select(b_path_sal = b_salience_num,
                    b_path_acc = b_accuracy_num)
  ) |>
  dplyr::mutate(
    indirect = a_path * b_path_acc,   # linear approximation
    direct   = b_path_sal
  )

indirect_conf <- draws_med |>
  dplyr::bind_cols(
    draws_conf |>
      dplyr::select(b_path_sal = b_salience_num,
                    b_path_acc = b_accuracy_num)
  ) |>
  dplyr::mutate(
    indirect = a_path * b_path_acc,
    direct   = b_path_sal
  )

# Summarise posterior
summarise_path <- function(draws, label) {
  draws |>
    dplyr::summarise(
      indirect_mean  = mean(indirect),
      indirect_lo95  = quantile(indirect, .025),
      indirect_hi95  = quantile(indirect, .975),
      direct_mean    = mean(direct),
      direct_lo95    = quantile(direct,   .025),
      direct_hi95    = quantile(direct,   .975),
      p_indirect_pos = mean(indirect > 0),
      p_direct_zero  = mean(abs(direct) < 0.05)   # P(|direct| < small threshold)
    ) |>
    dplyr::mutate(outcome = label)
}

brms_mediation_summary <- dplyr::bind_rows(
  summarise_path(indirect_arousal, "arousal"),
  summarise_path(indirect_conf,    "confidence")
)

cat("\n--- brms Mediation Summary (trial-level multilevel) ---\n")
print(brms_mediation_summary)

## 7e. Bayes Factor for direct effect being null (bridge sampling)
# Fit constrained model (direct path = 0) for BF comparison
bm_out_arousal_nodirect <- brms::brm(
  arousal_z ~ accuracy_num + abs_change + study_num + (1 | id),
  data        = test_b,
  family      = brms::gaussian(),
  prior       = bpriors,
  chains      = 4, iter = 4000, warmup = 2000,   # more iterations for bridge sampling
  cores       = 4, seed = 42,
  save_pars   = brms::save_pars(all = TRUE),
  file        = file.path(RESULTS_DIR, "brms_outcome_arousal_nodirect")
)

# Refit full model with save_pars for bridge sampling
bm_out_arousal_full_bs <- brms::brm(
  arousal_z ~ salience_num + accuracy_num + abs_change + study_num + (1 | id),
  data        = test_b,
  family      = brms::gaussian(),
  prior       = bpriors,
  chains      = 4, iter = 4000, warmup = 2000,
  cores       = 4, seed = 42,
  save_pars   = brms::save_pars(all = TRUE),
  file        = file.path(RESULTS_DIR, "brms_outcome_arousal_full_bs")
)

bf_direct_brms <- brms::bayes_factor(bm_out_arousal_nodirect,
                                      bm_out_arousal_full_bs)
cat("\nBF for no-direct-path model vs full model (arousal):\n")
print(bf_direct_brms)
cat("BF01 (null direct path):", round(bf_direct_brms$bf, 2), "\n")

## 7f. Save brms mediation summary
readr::write_csv(
  brms_mediation_summary,
  file.path(RESULTS_DIR, "brms_mediation_summary.csv")
)

# ============================================================
# 8. COMPARE FREQUENTIST vs BRMS RESULTS
# ============================================================
# Side-by-side summary of key estimates from both approaches.

freq_direct_arousal <- broom.mixed::tidy(m_arousal_full, effects = "fixed") |>
  dplyr::filter(term == "salience_flow") |>
  dplyr::transmute(
    approach = "frequentist",
    outcome  = "arousal",
    estimate = round(estimate, 3),
    ci_lo    = round(estimate - 1.96 * std.error, 3),
    ci_hi    = round(estimate + 1.96 * std.error, 3),
    p_or_pd  = round(p.value, 4)
  )

freq_direct_conf <- broom.mixed::tidy(m_conf_full, effects = "fixed") |>
  dplyr::filter(term == "salience_flow") |>
  dplyr::transmute(
    approach = "frequentist",
    outcome  = "confidence",
    estimate = round(estimate, 3),
    ci_lo    = round(estimate - 1.96 * std.error, 3),
    ci_hi    = round(estimate + 1.96 * std.error, 3),
    p_or_pd  = round(p.value, 4)
  )

brms_direct_arousal <- tidybayes::spread_draws(bm_out_arousal, b_salience_num) |>
  dplyr::summarise(
    approach = "brms",
    outcome  = "arousal",
    estimate = round(mean(b_salience_num), 3),
    ci_lo    = round(quantile(b_salience_num, .025), 3),
    ci_hi    = round(quantile(b_salience_num, .975), 3),
    p_or_pd  = round(mean(b_salience_num > 0), 3)   # P(direction)
  )

brms_direct_conf <- tidybayes::spread_draws(bm_out_conf, b_salience_num) |>
  dplyr::summarise(
    approach = "brms",
    outcome  = "confidence",
    estimate = round(mean(b_salience_num), 3),
    ci_lo    = round(quantile(b_salience_num, .025), 3),
    ci_hi    = round(quantile(b_salience_num, .975), 3),
    p_or_pd  = round(mean(b_salience_num > 0), 3)
  )

comparison_table <- dplyr::bind_rows(
  freq_direct_arousal, freq_direct_conf,
  brms_direct_arousal, brms_direct_conf
) |>
  dplyr::arrange(outcome, approach)

cat("\n--- Direct Salience Effect: Frequentist vs brms ---\n")
cat("(p_or_pd = p-value for frequentist; P(beta > 0) for brms)\n")
print(comparison_table)

readr::write_csv(
  comparison_table,
  file.path(RESULTS_DIR, "freq_vs_brms_direct_effect.csv")
)

# ============================================================
# 9. VISUALIZATION
# ============================================================

## 7a. Arousal and confidence by salience, split hit/miss
p_arousal <- ggplot2::ggplot(
  test,
  ggplot2::aes(x = salience_f, y = arousal_z, colour = accuracy_f, fill = accuracy_f)
) +
  ggplot2::stat_summary(fun = mean, geom = "bar", position = "dodge",
                        alpha = 0.6, width = 0.6) +
  ggplot2::stat_summary(fun.data = mean_cl_boot, geom = "errorbar",
                        position = ggplot2::position_dodge(0.6), width = 0.2) +
  ggplot2::facet_wrap(~ study_f) +
  ggplot2::scale_colour_manual(values = c("miss" = "#4C72B0", "hit" = "#DD8452")) +
  ggplot2::scale_fill_manual(  values = c("miss" = "#4C72B0", "hit" = "#DD8452")) +
  ggplot2::labs(
    x = "Salience", y = "Arousal (z)", colour = "Detection", fill = "Detection",
    title = "Test Block: Arousal by Salience and Detection"
  ) +
  ggplot2::theme_classic(base_size = 12)

p_conf <- p_arousal +
  ggplot2::aes(y = confidence_z) +
  ggplot2::labs(y = "Confidence (z)",
                title = "Test Block: Confidence by Salience and Detection")

p_combined <- p_arousal / p_conf
ggplot2::ggsave(
  file.path(RESULTS_DIR, "test_block_arousal_confidence.png"),
  p_combined, width = 8, height = 8, dpi = 300
)

## 9b. Posterior distributions for direct vs indirect effects (brms)
posterior_plot_data <- dplyr::bind_rows(
  indirect_arousal |>
    dplyr::select(indirect, direct) |>
    tidyr::pivot_longer(everything(), names_to = "path", values_to = "value") |>
    dplyr::mutate(outcome = "arousal"),
  indirect_conf |>
    dplyr::select(indirect, direct) |>
    tidyr::pivot_longer(everything(), names_to = "path", values_to = "value") |>
    dplyr::mutate(outcome = "confidence")
)

p_posterior <- ggplot2::ggplot(
  posterior_plot_data,
  ggplot2::aes(x = value, fill = path, colour = path)
) +
  ggplot2::geom_density(alpha = 0.4) +
  ggplot2::geom_vline(xintercept = 0, linetype = "dashed", colour = "grey40") +
  ggplot2::facet_wrap(~ outcome, scales = "free") +
  ggplot2::scale_fill_manual(
    values = c("indirect" = "#DD8452", "direct" = "#4C72B0"),
    labels = c("indirect" = "Indirect (via detection)", "direct" = "Direct")
  ) +
  ggplot2::scale_colour_manual(
    values = c("indirect" = "#DD8452", "direct" = "#4C72B0"),
    labels = c("indirect" = "Indirect (via detection)", "direct" = "Direct")
  ) +
  ggplot2::labs(
    x = "Posterior estimate", y = "Density",
    fill = "Path", colour = "Path",
    title = "Posterior: Salience -> Arousal/Confidence",
    subtitle = "Indirect path (via detection) vs direct path"
  ) +
  ggplot2::theme_classic(base_size = 12)

ggplot2::ggsave(
  file.path(RESULTS_DIR, "brms_posterior_mediation.png"),
  p_posterior, width = 9, height = 5, dpi = 300
)

## 9c. Mediation path diagram values (print for reporting)
cat("\n--- Frequentist Mediation Summary: Salience -> Accuracy -> Arousal ---\n")
cat("ACME (indirect):", round(med_result$d0, 3),
    "95% CI [", round(med_result$d0.ci[1], 3), ",",
    round(med_result$d0.ci[2], 3), "]\n")
cat("ADE (direct):   ", round(med_result$z0, 3),
    "95% CI [", round(med_result$z0.ci[1], 3), ",",
    round(med_result$z0.ci[2], 3), "]\n")
cat("Prop. mediated: ", round(med_result$n0, 3), "\n")

# ============================================================
# 10. SAVE FREQUENTIST RESULTS TABLE
# ============================================================
results_table <- dplyr::bind_rows(
  # Marginal salience effects
  broom.mixed::tidy(m_arousal_sal, effects = "fixed") |>
    dplyr::filter(term == "salience_flow") |>
    dplyr::mutate(model = "arousal_marginal"),
  broom.mixed::tidy(m_conf_sal, effects = "fixed") |>
    dplyr::filter(term == "salience_flow") |>
    dplyr::mutate(model = "confidence_marginal"),
  # After conditioning on accuracy
  broom.mixed::tidy(m_arousal_full, effects = "fixed") |>
    dplyr::filter(term %in% c("salience_flow", "accuracy_fhit")) |>
    dplyr::mutate(model = "arousal_full"),
  broom.mixed::tidy(m_conf_full, effects = "fixed") |>
    dplyr::filter(term %in% c("salience_flow", "accuracy_fhit")) |>
    dplyr::mutate(model = "confidence_full")
) |>
  dplyr::mutate(
    partial_r = statistic / sqrt(statistic^2 + df),
    across(where(is.numeric), \(x) round(x, 4))
  ) |>
  dplyr::select(model, term, estimate, std.error, statistic, df, p.value, partial_r)

readr::write_csv(results_table,
                 file.path(RESULTS_DIR, "test_block_salience_arousal_results.csv"))

cat("\nDone. Files written to:", RESULTS_DIR, "\n")
cat("  test_block_salience_arousal_results.csv  -- frequentist fixed effects\n")
cat("  brms_mediation_summary.csv               -- brms indirect/direct path posteriors\n")
cat("  freq_vs_brms_direct_effect.csv           -- side-by-side comparison\n")
cat("  test_block_arousal_confidence.png        -- bar plot by salience x detection\n")
cat("  brms_posterior_mediation.png             -- posterior density: indirect vs direct\n")
cat("  brms_*.rds                               -- cached brms model objects\n")

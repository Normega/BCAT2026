# Test Block Arousal and Confidence Analysis
# Examines whether salience manipulation affects arousal and confidence in test blocks
# (Studies 4 and 5), complementing existing accuracy analyses (H5)
#
# Prediction: low-salience trials (tested at high-salience threshold) produce
# lower detection rates, and thereby lower arousal and confidence.
# Key tests:
#   (1) Marginal salience effect on arousal and confidence
#   (2) Salience effect after conditioning on hit/miss
#   (3) Mediation: salience -> detection -> arousal (frequentist + brms)
#   (4) Group interactions: does salience x accuracy pattern differ by Breath vs Visual?

# Set Up ---------
## Load libraries ---------
packages <- c(
  "tidyverse",
  "lme4",
  "lmerTest",
  "car",
  "ggeffects",
  "BayesFactor",
  "brms",
  "posterior",
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
DATA_DIR    <- file.path(BASE_DIR, "Data")
RESULTS_DIR <- file.path(BASE_DIR, "Results")
RDS_DIR <- file.path(RESULTS_DIR, "Models", "TestRDS")
FIGURES_DIR <- file.path(BASE_DIR, "Figures")
dir.create(RESULTS_DIR, showWarnings = FALSE, recursive = TRUE)

# ============================================================
# 1. LOAD AND HARMONIZE DATA
# ============================================================
# Study 4: Salience and Direction are all NaN -- derived from Condition string
#   e.g. "highSalienceAcc" -> salience = High, direction = Faster
#   Group: "Breath" | "Visual"
#   flag_zero_variance: exclude TRUE rows
#   Single session only
#
# Study 5: explicit Salience ("High"/"Low") and Direction ("Faster"/"Slower")
#   Group derived from Condition: "breath" -> "Breath", "visual" -> "Visual"
#   ses: "ses1" | "ses2" (nested as random effect)

s4_raw <- readr::read_csv(file.path(DATA_DIR, "study4_test.csv"))
s5_raw <- readr::read_csv(file.path(DATA_DIR, "study5_test.csv"))

s4 <- s4_raw |>
  dplyr::filter(!flag_zero_variance) |>
  dplyr::mutate(
    study      = "S4",
    salience   = dplyr::if_else(grepl("^high", Condition, ignore.case = TRUE), "High", "Low"),
    direction  = dplyr::if_else(grepl("Acc$",  Condition), "Faster", "Slower"),
    group      = Group,                           # "Breath" | "Visual"
    abs_change = Level,
    ses        = "ses1"                           # S4 is single-session
  ) |>
  dplyr::select(id, study, ses, group, salience, direction, abs_change,
                Accuracy, Confidence, Arousal)

s5 <- s5_raw |>
  dplyr::mutate(
    study      = "S5",
    salience   = Salience,                        # "High" | "Low"
    direction  = Direction,                       # "Faster" | "Slower"
    group      = dplyr::if_else(Condition == "breath", "Breath", "Visual"),
    abs_change = level,
    ses        = ses
  ) |>
  dplyr::select(id, study, ses, group, salience, direction, abs_change,
                Accuracy, Confidence, Arousal)

# Combine and recode
test <- dplyr::bind_rows(s4, s5) |>
  dplyr::rename(
    accuracy   = Accuracy,
    confidence = Confidence,
    arousal    = Arousal
  ) |>
  dplyr::mutate(
    salience_f  = factor(salience,  levels = c("High", "Low")),
    accuracy_f  = factor(accuracy,  levels = c(0, 1), labels = c("miss", "hit")),
    direction_f = factor(direction, levels = c("Faster", "Slower")),
    group_f     = factor(group,     levels = c("Breath", "Visual")),
    study_f     = factor(study,     levels = c("S4", "S5")),
    ses_f       = factor(ses)
  ) |>
  # Z-score arousal and confidence within participant x study
  dplyr::ungroup()

cat("Trial counts by study, group, salience:\n")
test |>
  dplyr::count(study, group_f, salience_f) |>
  print()

cat("\nParticipant counts by study and group:\n")
test |>
  dplyr::distinct(id, study, group_f) |>
  dplyr::count(study, group_f) |>
  print()

# Numeric coding for brms
test_b <- test |>
  dplyr::mutate(
    salience_num = dplyr::if_else(salience_f == "High", 1L, 0L),
    accuracy_num = accuracy,
    group_num    = dplyr::if_else(group_f == "Breath", 1L, 0L),
    study_num    = dplyr::if_else(study_f == "S5",    1L, 0L)
  )

# ============================================================
# 2. HELPERS
# ============================================================
partial_r <- function(model, term) {
  tt    <- summary(model)$coefficients
  t_val <- tt[term, "t value"]
  df    <- tt[term, "df"]
  r     <- t_val / sqrt(t_val^2 + df)
  ci_lo <- tanh(atanh(r) - 1.96 / sqrt(df - 3))
  ci_hi <- tanh(atanh(r) + 1.96 / sqrt(df - 3))
  tibble::tibble(term = term, partial_r = round(r, 3),
                 ci_lo = round(ci_lo, 3), ci_hi = round(ci_hi, 3))
}

# bobyqa optimizer with tightened gradient tolerance -- use for all lmer calls
lmer_ctrl <- lme4::lmerControl(
  optimizer = "bobyqa",
  optCtrl   = list(maxfun = 2e5)
)

# ============================================================
# 3. ANALYSIS 1: MARGINAL SALIENCE EFFECT
# ============================================================
# Does salience alone predict arousal and confidence?
# Singular fit with nested (1|id/ses_f) -- (1|id) is sufficient.

m_arousal_sal <- lmerTest::lmer(
  arousal ~ salience_f + study_f +
    (1 | id),
  data = test, REML = FALSE, control = lmer_ctrl
)
summary(m_arousal_sal)

m_conf_sal <- lmerTest::lmer(
  confidence ~ salience_f + study_f +
    (1 | id),
  data = test, REML = FALSE, control = lmer_ctrl
)
summary(m_conf_sal)

marginal_effects <- dplyr::bind_rows(
  partial_r(m_arousal_sal, "salience_fLow") |> dplyr::mutate(outcome = "arousal"),
  partial_r(m_conf_sal,    "salience_fLow") |> dplyr::mutate(outcome = "confidence")
)
cat("\nMarginal salience effects:\n"); print(marginal_effects)

# ============================================================
# 4. ANALYSIS 2: SALIENCE CONDITIONAL ON HIT/MISS
# ============================================================
# If awareness-gating is the full story, salience_f drops out
# once accuracy_f is included.

m_arousal_full <- lmerTest::lmer(
  arousal ~ salience_f * accuracy_f + study_f +
    (1 | id),
  data = test, REML = FALSE, control = lmer_ctrl
)
summary(m_arousal_full)

m_conf_full <- lmerTest::lmer(
  confidence ~ salience_f * accuracy_f + study_f +
    (1 | id),
  data = test, REML = FALSE, control = lmer_ctrl
)
summary(m_conf_full)

lrt_arousal <- anova(m_arousal_sal, m_arousal_full)
lrt_conf    <- anova(m_conf_sal,    m_conf_full)
cat("\nLRT arousal (marginal vs +accuracy):\n");    print(lrt_arousal)
cat("\nLRT confidence (marginal vs +accuracy):\n"); print(lrt_conf)

# ============================================================
# 5. ANALYSIS 3: GROUP INTERACTIONS
# ============================================================
# Key theoretical test: does the salience x accuracy (awareness-gating)
# pattern differ between Breath and Visual groups?
#
# Predictions:
#   Breath:  strong salience x accuracy interaction (gating of interoceptive signal)
#   Visual:  salience effect absent or not moderated by accuracy
#            (no interoceptive signal to gate)
#
# Three models:
#   5a. salience x group          (marginal group moderation)
#   5b. salience x accuracy x group (three-way: is gating Breath-specific?)
#   5c. simple effects within each group

## 5a. Marginal: does the salience effect differ by group?
m_arousal_grp <- lmerTest::lmer(
  arousal ~ salience_f * group_f + study_f +
    (1 | id),
  data = test, REML = FALSE, control = lmer_ctrl
)
summary(m_arousal_grp)

m_conf_grp <- lmerTest::lmer(
  confidence ~ salience_f * group_f + study_f +
    (1 | id),
  data = test, REML = FALSE, control = lmer_ctrl
)
summary(m_conf_grp)

cat("\nType III ANOVA -- Group x Salience (arousal):\n")
car::Anova(m_arousal_grp, type = 3) |> print()
cat("\nType III ANOVA -- Group x Salience (confidence):\n")
car::Anova(m_conf_grp, type = 3) |> print()

## 5b. Three-way: salience x accuracy x group
m_arousal_3way <- lmerTest::lmer(
  arousal ~ salience_f * accuracy_f * group_f +
    study_f +
    (1 | id),
  data = test, REML = FALSE, control = lmer_ctrl
)
summary(m_arousal_3way)

m_conf_3way <- lmerTest::lmer(
  confidence ~ salience_f * accuracy_f * group_f +
    study_f +
    (1 | id),
  data = test, REML = FALSE, control = lmer_ctrl
)
summary(m_conf_3way)

# LRT: does group moderation improve on two-way model?
lrt_3way_arousal <- anova(m_arousal_full, m_arousal_3way)
lrt_3way_conf    <- anova(m_conf_full,    m_conf_3way)
cat("\nLRT: two-way vs three-way (arousal):\n");    print(lrt_3way_arousal)
cat("\nLRT: two-way vs three-way (confidence):\n"); print(lrt_3way_conf)

## 5c. Simple effects within each group
for (grp in c("Breath", "Visual")) {
  cat(sprintf("\n--- Simple effects: %s group ---\n", grp))
  df_grp <- dplyr::filter(test, group_f == grp)
  
  m_a <- lmerTest::lmer(
    arousal ~ salience_f * accuracy_f + study_f +
      (1 | id),
    data = df_grp, REML = FALSE, control = lmer_ctrl
  )
  m_c <- lmerTest::lmer(
    confidence ~ salience_f * accuracy_f + study_f +
      (1 | id),
    data = df_grp, REML = FALSE, control = lmer_ctrl
  )
  cat(sprintf("Arousal -- %s:\n", grp));    print(summary(m_a)$coefficients)
  cat(sprintf("Confidence -- %s:\n", grp)); print(summary(m_c)$coefficients)
}

# ============================================================
# 6. ANALYSIS 4: FREQUENTIST MEDIATION BY GROUP (person-level)
# ============================================================
person_test <- test |>
  dplyr::group_by(id, study, group_f, salience_f) |>
  dplyr::summarise(
    mean_arousal    = mean(arousal,    na.rm = TRUE),
    mean_confidence = mean(confidence, na.rm = TRUE),
    mean_accuracy   = mean(accuracy,     na.rm = TRUE),
    n_trials        = dplyr::n(),
    .groups         = "drop"
  ) |>
  dplyr::mutate(salience_num = dplyr::if_else(salience_f == "High", 1, 0))

run_mediation <- function(data, outcome_var, label, n_boot = 1000) {
  keep <- !is.na(data$mean_accuracy)  & !is.nan(data$mean_accuracy) &
    !is.na(data[[outcome_var]]) & !is.nan(data[[outcome_var]])
  data <- data[keep, ]
  
  out_fml <- paste(outcome_var, "~ salience_num + mean_accuracy")
  
  # Point estimates
  a_est  <- coef(lm(mean_accuracy ~ salience_num, data = data))[["salience_num"]]
  out_pt <- coef(lm(as.formula(out_fml), data = data))
  b_est  <- out_pt[["mean_accuracy"]]
  d_est  <- out_pt[["salience_num"]]
  indirect_est <- a_est * b_est
  
  # Percentile bootstrap CIs
  set.seed(42)
  boot_indirect <- replicate(n_boot, {
    db   <- data[sample(nrow(data), replace = TRUE), ]
    a_b  <- coef(lm(mean_accuracy ~ salience_num, data = db))[["salience_num"]]
    b_b  <- coef(lm(as.formula(out_fml), data = db))[["mean_accuracy"]]
    a_b * b_b
  })
  
  cat(sprintf("\n--- Mediation: %s (%s) ---\n", outcome_var, label))
  cat(sprintf("  a (sal->acc):    %.3f\n", a_est))
  cat(sprintf("  b (acc->out):    %.3f\n", b_est))
  cat(sprintf("  Indirect (a*b):  %.3f [%.3f, %.3f]\n",
              indirect_est,
              quantile(boot_indirect, .025),
              quantile(boot_indirect, .975)))
  cat(sprintf("  Direct:          %.3f\n", d_est))
  
  tibble::tibble(
    group    = label,
    outcome  = outcome_var,
    indirect = round(indirect_est, 3),
    ind_lo   = round(quantile(boot_indirect, .025), 3),
    ind_hi   = round(quantile(boot_indirect, .975), 3),
    direct   = round(d_est, 3),
    prop_med = round(indirect_est / (indirect_est + d_est), 3)
  )
}

mediation_results <- purrr::map_dfr(
  c("Breath", "Visual"),
  function(grp) {
    df_grp <- dplyr::filter(person_test, group_f == grp)
    dplyr::bind_rows(
      run_mediation(df_grp, "mean_arousal",    grp),
      run_mediation(df_grp, "mean_confidence", grp)
    )
  }
)
cat("\n--- Mediation summary by group ---\n"); print(mediation_results)

# ============================================================
# 7. BRMS: MULTILEVEL MEDIATION WITH GROUP INTERACTION
# ============================================================
bpriors <- c(
  brms::prior(normal(0, 1),   class = "b"),
  brms::prior(normal(0, 1),   class = "Intercept"),
  brms::prior(exponential(1), class = "sd"),
  brms::prior(exponential(1), class = "sigma")
)

## 7a. Mediator: salience x group -> accuracy (logistic)
bm_med <- brms::brm(
  accuracy_num ~ salience_num * group_num + study_num +
    (1 | id),
  data   = test_b,
  family = brms::bernoulli(link = "logit"),
  prior  = bpriors[bpriors$class != "sigma", ],
  chains = 4, iter = 2000, warmup = 1000,
  cores  = 4, seed = 42,
  file   = file.path(RDS_DIR, "brms_mediator_group")
)
summary(bm_med)

## 7b. Outcome: arousal ~ salience x group + accuracy x group
bm_out_arousal <- brms::brm(
  arousal ~ salience_num * group_num + accuracy_num * group_num +
    study_num + (1 | id),
  data   = test_b,
  family = gaussian(),
  prior  = bpriors,
  chains = 4, iter = 2000, warmup = 1000,
  cores  = 4, seed = 42,
  file   = file.path(RDS_DIR, "brms_outcome_arousal_group")
)
summary(bm_out_arousal)

## 7c. Outcome: confidence ~ salience x group + accuracy x group
bm_out_conf <- brms::brm(
  confidence ~ salience_num * group_num + accuracy_num * group_num +
    study_num + (1 | id),
  data   = test_b,
  family = gaussian(),
  prior  = bpriors,
  chains = 4, iter = 2000, warmup = 1000,
  cores  = 4, seed = 42,
  file   = file.path(RDS_DIR, "brms_outcome_confidence_group")
)
summary(bm_out_conf)

## 7d. Group-specific indirect effects from posterior draws
# as_draws_df avoids tidybayes spec-parser issues with colons in parameter names
get_draws <- function(model, pattern) {
  df <- posterior::as_draws_df(model)
  dplyr::select(df, dplyr::matches(pattern))
}

draws_med_df <- posterior::as_draws_df(bm_med)
b_params_med <- grep("^b_", names(draws_med_df), value = TRUE)
cat("\nMediator model b_ parameters:\n"); print(b_params_med)
sal_col     <- grep("b_salience_num$",                         names(draws_med_df), value = TRUE)
sal_grp_col <- grep("b_.*salience.*group|b_.*group.*salience", names(draws_med_df), value = TRUE)

draws_med <- tibble::tibble(
  b_sal     = draws_med_df[[sal_col]],
  b_sal_grp = draws_med_df[[sal_grp_col]]
) |>
  dplyr::mutate(
    a_breath = b_sal + b_sal_grp,
    a_visual = b_sal
  )

compute_indirect <- function(outcome_model, draws_med, outcome_label) {
  out_df      <- posterior::as_draws_df(outcome_model)
  
  # Diagnostic: print available b_ parameters so naming is transparent
  b_params <- grep("^b_", names(out_df), value = TRUE)
  cat("\nbrms parameters in", outcome_label, "model:\n")
  print(b_params)
  
  acc_col     <- grep("b_accuracy_num$",               names(out_df), value = TRUE)
  acc_grp_col <- grep("b_.*accuracy.*group|b_.*group.*accuracy", names(out_df), value = TRUE)
  
  if (length(acc_grp_col) == 0)
    stop("Cannot find accuracy:group interaction term. Available: ",
         paste(b_params, collapse = ", "))
  
  draws_out <- tibble::tibble(
    b_acc     = out_df[[acc_col]],
    b_acc_grp = out_df[[acc_grp_col]]
  ) |>
    dplyr::mutate(
      b_breath = b_acc + b_acc_grp,
      b_visual = b_acc
    )
  
  draws_combined <- dplyr::bind_cols(
    draws_med  |> dplyr::select(a_breath, a_visual),
    draws_out  |> dplyr::select(b_breath, b_visual)
  ) |>
    dplyr::mutate(
      indirect_breath = a_breath * b_breath,
      indirect_visual = a_visual * b_visual,
      indirect_diff   = indirect_breath - indirect_visual  # Breath - Visual
    )
  
  summary <- draws_combined |>
    dplyr::summarise(
      dplyr::across(
        c(indirect_breath, indirect_visual, indirect_diff),
        list(mean = mean,
             lo95 = ~ quantile(.x, .025),
             hi95 = ~ quantile(.x, .975),
             pd   = ~ mean(.x > 0)),
        .names = "{.col}_{.fn}"
      )
    ) |>
    dplyr::mutate(outcome = outcome_label)
  
  list(summary = summary, draws = draws_combined)
}

brms_indirect_raw <- list(
  arousal    = compute_indirect(bm_out_arousal, draws_med, "arousal"),
  confidence = compute_indirect(bm_out_conf,    draws_med, "confidence")
)

brms_indirect <- dplyr::bind_rows(
  brms_indirect_raw$arousal$summary,
  brms_indirect_raw$confidence$summary
)

# Print full indirect summary with group difference
cat("\n--- brms indirect effects (Breath, Visual, Breath - Visual) ---\n")
brms_indirect |>
  dplyr::select(outcome,
                ends_with("breath_mean"), ends_with("breath_lo95"), ends_with("breath_hi95"),
                ends_with("visual_mean"), ends_with("visual_lo95"), ends_with("visual_hi95"),
                ends_with("diff_mean"),   ends_with("diff_lo95"),   ends_with("diff_hi95"),
                ends_with("diff_pd")) |>
  print(width = 120)

# Posterior probability that Breath indirect > Visual indirect (for arousal)
cat(sprintf(
  "\nP(indirect_breath > indirect_visual) for arousal: %.3f\n",
  mean(brms_indirect_raw$arousal$draws$indirect_breath >
         brms_indirect_raw$arousal$draws$indirect_visual)
))
cat(sprintf(
  "Posterior diff (Breath - Visual): %.3f [%.3f, %.3f]\n",
  mean(brms_indirect_raw$arousal$draws$indirect_diff),
  quantile(brms_indirect_raw$arousal$draws$indirect_diff, .025),
  quantile(brms_indirect_raw$arousal$draws$indirect_diff, .975)
))

## 7e. BF for null direct salience path (bridge sampling)
bm_out_arousal_bs <- brms::brm(
  arousal ~ salience_num * group_num + accuracy_num * group_num +
    study_num + (1 | id),
  data      = test_b, family = gaussian(), prior = bpriors,
  chains = 4, iter = 4000, warmup = 2000, cores = 4, seed = 42,
  save_pars = brms::save_pars(all = TRUE),
  file      = file.path(RDS_DIR, "brms_arousal_group_bs")
)

bm_out_arousal_nodirect <- brms::brm(
  arousal ~ accuracy_num * group_num + study_num +
    (1 | id),
  data      = test_b, family = gaussian(), prior = bpriors,
  chains = 4, iter = 4000, warmup = 2000, cores = 4, seed = 42,
  save_pars = brms::save_pars(all = TRUE),
  file      = file.path(RDS_DIR, "brms_arousal_nodirect_group")
)

bf_direct <- brms::bayes_factor(bm_out_arousal_nodirect, bm_out_arousal_bs)
cat("\nBF01 for null direct salience path (arousal, with group):",
    round(bf_direct$bf, 2), "\n")

# ============================================================
# 8. COMPARE FREQUENTIST vs BRMS: KEY TERMS
# ============================================================
freq_3way <- broom.mixed::tidy(m_arousal_3way, effects = "fixed") |>
  dplyr::transmute(
    approach = "frequentist", outcome = "arousal", term,
    estimate = round(estimate, 3),
    ci_lo    = round(estimate - 1.96 * std.error, 3),
    ci_hi    = round(estimate + 1.96 * std.error, 3),
    p_or_pd  = round(p.value, 4)
  )

brms_key <- local({
  df          <- posterior::as_draws_df(bm_out_arousal)
  acc_col     <- grep("b_accuracy_num$",                         names(df), value = TRUE)
  acc_grp_col <- grep("b_.*accuracy.*group|b_.*group.*accuracy", names(df), value = TRUE)
  acc_vec     <- df[[acc_col]]
  grp_vec     <- df[[acc_grp_col]]
  dplyr::bind_rows(
    tibble::tibble(
      approach = "brms", outcome = "arousal", term = "accuracy_num",
      estimate = round(mean(acc_vec), 3),
      ci_lo    = round(quantile(acc_vec, .025), 3),
      ci_hi    = round(quantile(acc_vec, .975), 3),
      p_or_pd  = round(mean(acc_vec > 0), 3)
    ),
    tibble::tibble(
      approach = "brms", outcome = "arousal", term = "accuracy_num:group_num",
      estimate = round(mean(grp_vec), 3),
      ci_lo    = round(quantile(grp_vec, .025), 3),
      ci_hi    = round(quantile(grp_vec, .975), 3),
      p_or_pd  = round(mean(grp_vec > 0), 3)
    )
  )
})

comparison_table <- dplyr::bind_rows(freq_3way, brms_key) |>
  dplyr::arrange(term, approach)
cat("\n--- Key terms: frequentist vs brms ---\n"); print(comparison_table)

# ============================================================
# 9. VISUALIZATION
# ============================================================

## 9a. Arousal and confidence: salience x hit/miss x group
make_bar_plot <- function(outcome_var, ylabel, title_str) {
  ggplot2::ggplot(
    test,
    ggplot2::aes(x = salience_f, y = .data[[outcome_var]],
                 colour = accuracy_f, fill = accuracy_f)
  ) +
    ggplot2::stat_summary(fun = mean, geom = "bar",
                          position = "dodge", alpha = 0.6, width = 0.6) +
    ggplot2::stat_summary(fun.data = mean_cl_boot, geom = "errorbar",
                          position = ggplot2::position_dodge(0.6), width = 0.2) +
    ggplot2::facet_grid(study_f ~ group_f) +
    ggplot2::scale_colour_manual(values = c("miss" = "#4C72B0", "hit" = "#DD8452")) +
    ggplot2::scale_fill_manual(  values = c("miss" = "#4C72B0", "hit" = "#DD8452")) +
    ggplot2::labs(x = "Salience", y = ylabel,
                  colour = "Detection", fill = "Detection", title = title_str) +
    ggplot2::theme_classic(base_size = 12) +
    ggplot2::theme(strip.background = ggplot2::element_blank())
}

p_combined <- make_bar_plot("arousal",    "Arousal (1-6)",    "Arousal: Salience x Detection x Group") /
  make_bar_plot("confidence", "Confidence (1-6)", "Confidence: Salience x Detection x Group")

ggplot2::ggsave(
  file.path(FIGURES_DIR, "test_block_arousal_confidence_group.png"),
  p_combined, width = 10, height = 10, dpi = 300
)

## 9b. Posterior indirect effects by group (arousal)
# Re-use draws already computed in compute_indirect -- no need to re-extract
arousal_draws_plot <- brms_indirect_raw$arousal$draws |>
  dplyr::select(indirect_breath, indirect_visual, indirect_diff) |>
  tidyr::pivot_longer(everything(), names_to = "path", values_to = "value") |>
  dplyr::mutate(path = dplyr::recode(path,
                                     indirect_breath = "Breath",
                                     indirect_visual = "Visual",
                                     indirect_diff   = "Breath - Visual"
  ))

p_posterior <- ggplot2::ggplot(
  dplyr::filter(arousal_draws_plot, path != "Breath - Visual"),
  ggplot2::aes(x = value, fill = path, colour = path)
) +
  ggplot2::geom_density(alpha = 0.4) +
  ggplot2::geom_vline(xintercept = 0, linetype = "dashed", colour = "grey40") +
  ggplot2::scale_fill_manual(  values = c("Breath" = "#DD8452", "Visual" = "#4C72B0")) +
  ggplot2::scale_colour_manual(values = c("Breath" = "#DD8452", "Visual" = "#4C72B0")) +
  ggplot2::labs(
    x = "Indirect effect (salience -> detection -> arousal)",
    y = "Density", fill = "Group", colour = "Group",
    title = "Posterior: Group-specific indirect effects on arousal"
  ) +
  ggplot2::theme_classic(base_size = 12)

p_diff <- ggplot2::ggplot(
  dplyr::filter(arousal_draws_plot, path == "Breath - Visual"),
  ggplot2::aes(x = value)
) +
  ggplot2::geom_density(fill = "#59A14F", colour = "#59A14F", alpha = 0.4) +
  ggplot2::geom_vline(xintercept = 0, linetype = "dashed", colour = "grey40") +
  ggplot2::labs(
    x = "Difference in indirect effect (Breath - Visual)",
    y = "Density",
    title = "Posterior: Breath vs Visual indirect effect difference (arousal)"
  ) +
  ggplot2::theme_classic(base_size = 12)

ggplot2::ggsave(
  file.path(FIGURES_DIR, "brms_posterior_indirect_group.png"),
  p_posterior / p_diff, width = 8, height = 8, dpi = 300
)

# ============================================================
# 10. SAVE ALL RESULTS
# ============================================================
results_table <- dplyr::bind_rows(
  broom.mixed::tidy(m_arousal_sal,  effects = "fixed") |> dplyr::mutate(model = "arousal_marginal"),
  broom.mixed::tidy(m_conf_sal,     effects = "fixed") |> dplyr::mutate(model = "confidence_marginal"),
  broom.mixed::tidy(m_arousal_full, effects = "fixed") |> dplyr::mutate(model = "arousal_full"),
  broom.mixed::tidy(m_conf_full,    effects = "fixed") |> dplyr::mutate(model = "confidence_full"),
  broom.mixed::tidy(m_arousal_grp,  effects = "fixed") |> dplyr::mutate(model = "arousal_group"),
  broom.mixed::tidy(m_conf_grp,     effects = "fixed") |> dplyr::mutate(model = "confidence_group"),
  broom.mixed::tidy(m_arousal_3way, effects = "fixed") |> dplyr::mutate(model = "arousal_3way"),
  broom.mixed::tidy(m_conf_3way,    effects = "fixed") |> dplyr::mutate(model = "confidence_3way")
) |>
  dplyr::mutate(
    partial_r = statistic / sqrt(statistic^2 + df),
    dplyr::across(where(is.numeric), \(x) round(x, 4))
  ) |>
  dplyr::select(model, term, estimate, std.error, statistic, df, p.value, partial_r)

readr::write_csv(results_table,
                 file.path(RESULTS_DIR, "test_block_all_models.csv"))
readr::write_csv(mediation_results,
                 file.path(RESULTS_DIR, "frequentist_mediation_by_group.csv"))
readr::write_csv(brms_indirect,
                 file.path(RESULTS_DIR, "brms_indirect_by_group.csv"))
readr::write_csv(brms_indirect_raw$arousal$draws,
                 file.path(RESULTS_DIR, "brms_arousal_indirect_draws.csv"))
readr::write_csv(comparison_table,
                 file.path(RESULTS_DIR, "freq_vs_brms_key_terms.csv"))

cat("\nDone. Files written to:", RESULTS_DIR, "\n")
cat("  test_block_all_models.csv                -- all frequentist fixed effects\n")
cat("  frequentist_mediation_by_group.csv       -- mediation indirect/direct by group\n")
cat("  brms_indirect_by_group.csv               -- brms posterior indirect effects\n")
cat("  freq_vs_brms_key_terms.csv               -- comparison table\n")
cat("  test_block_arousal_confidence_group.png  -- bar plots: salience x detection x group\n")
cat("  brms_posterior_indirect_group.png        -- posterior density by group\n")
cat("  brms_*.rds                               -- cached brms model objects\n")
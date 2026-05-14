# ============================================================
# MainAnalysis.R
# BCAT Five-Study Paper — Master Script
#
# Sets all paths once. Every analysis file reads BASE_DIR,
# DATA_DIR, ANALYSIS_DIR, RESULTS_DIR, FIG_DIR, MODEL_DIR
# from this environment — no paths are set anywhere else.
#
# Run order:
#   1. study{N}_clean.R scripts (data preparation)
#   2. Intero2025_PrepQualtrics.R (Study 5 questionnaires)
#   3. This script (sources all analysis files in order)
#
# PRIMARY RESULTS (main text order):
#   analysis_val_detection.R              — Task Validation: Change² (Table 2)
#   analysis_val_pilot_studies.R          — Supplement S1.1 / S1.2 / S1.3
#   analysis_val_thresholds.R             — Supplement S1.4 (H1, H2, H5, H6)
#   analysis_arousal.R                    — Awareness Gates Arousal Transfer
#   analysis_miss_baseline.R              — Bayesian null: misses vs. baseline
#   analysis_study3_attraction_mediation.R — Study 3 misattribution chain
#   analysis_maia.R                       — MAIA: sensibility vs. sensitivity
#
# SUPPLEMENTARY (supplement order):
#   analysis_tce.R                        — S2: TCE sensitivity analyses
#   analysis_individual_differences.R     — S3: individual differences
#   analysis_belt.R                       — S6: belt entrainment + physio
#   belt_salience_followup.R              — S6: belt salience follow-up
#   analysis_s6_entrainment.R             — S6: belt-pacer entrainment -> detection
#   analysis_study5_exploratory.R         — exploratory Study 5
#   analysis_hbd.R                        — HBD cardiac exploratory
#
# Shared objects available to all sourced files:
#   Data:    s1l, s1s, s2l, s2s, s3l, s3s, s4l, s4s, s4t,
#            s5l, s5s, s5t, s5_long_breath, s1l_A_sorted
#   Paths:   BASE_DIR, DATA_DIR, ANALYSIS_DIR, RESULTS_DIR,
#            FIG_DIR, MODEL_DIR
#   Helpers: partial_r_from_t(), add_odds_ratios(), add_partial_r(),
#            extract_change2_results(), compute_test_dprime_3afc(),
#            make_threshold_long(), compute_retest_icc(), %||%
#            apply_bh_correction() — all defined in utils.R
# ============================================================

# ── Packages ──────────────────────────────────────────────────
packages <- c(
  "mediation", "bridgesampling",
  "tidyverse", "readxl", "lme4", "lmerTest",
  "emmeans", "BayesFactor", 
  "ppcor",
  "broom.mixed",
  "MuMIn", "irr", "metafor", "patchwork", "ggeffects",
  "brms", "tidybayes"
)
new_packages <- packages[!sapply(packages, requireNamespace, quietly = TRUE)]
if (length(new_packages)) install.packages(new_packages)
options(readr.show_col_types = FALSE,
        dplyr.summarise.inform = FALSE)

for (thispack in packages) {
  library(thispack, character.only = TRUE, quietly = TRUE, verbose = FALSE)
}


# ============================================================
# Paths — set once here; all sourced files use these objects
# ============================================================
BASE_DIR     <- "I:/Shared drives/Interoception 2025/Repo/"
DATA_DIR     <- paste0(BASE_DIR, "Data/")
ANALYSIS_DIR <- paste0(BASE_DIR, "Analysis/")
RESULTS_DIR  <- paste0(BASE_DIR, "Results/")
FIG_DIR      <- paste0(RESULTS_DIR, "Figures/")
MODEL_DIR    <- paste0(RESULTS_DIR, "Models/")

for (.d in c(RESULTS_DIR, FIG_DIR, MODEL_DIR)) {
  dir.create(.d, showWarnings = FALSE, recursive = TRUE)
}
rm(.d)

# ── Utility scripts ───────────────────────────────────────────
# utils.R:        data loading, effect size helpers, reshape helpers
# theme_bcat.R:   shared ggplot theme
# meta_analysis.R: meta-analytic pooling helpers
source(paste0(ANALYSIS_DIR, "utils.R"))
source(paste0(ANALYSIS_DIR, "theme_bcat.R"))
source(paste0(ANALYSIS_DIR, "meta_analysis.R"))


# ── Data loading and standardisation ──────────────────────────
message("Loading and standardising data...")

d <- load_all_data()

for (study in 1:5) {
  key_l <- paste0("s", study, "_long")
  key_s <- paste0("s", study, "_summary")
  if (key_l %in% names(d))
    d[[key_l]] <- standardise_study_data(d[[key_l]], study)
  if (key_s %in% names(d))
    d[[key_s]] <- standardise_study_data(d[[key_s]], study) |>
      standardise_maia(study_label = paste("Study", study))
}

s1l <- d$s1_long;  s1s <- d$s1_summary
s2l <- d$s2_long;  s2s <- d$s2_summary
s3l <- d$s3_long;  s3s <- d$s3_summary
s4l <- d$s4_long;  s4s <- d$s4_summary;  s4t <- d$s4_test
s5l <- d$s5_long;  s5s <- d$s5_summary;  s5t <- d$s5_test

# Study 5 belt QC (used by analysis_belt.R, belt_salience_followup.R,
#                   analysis_s6_entrainment.R)
qcFull    <- d$s5_qcFull
qcSummary <- d$s5_qcSummary

# Study 5 HBD (used by analysis_hbd.R)
s5_hbd           <- d$s5_hbd
s5_hbd_intervals <- d$s5_hbd_intervals

# Parse Salience and Direction from Condition strings in test files
s4t <- s4t |>
  dplyr::mutate(
    Salience  = dplyr::if_else(stringr::str_starts(Condition,     "high"), "High", "Low"),
    Direction = dplyr::if_else(stringr::str_ends(Condition,       "Acc"),  "Faster", "Slower")
  )
s5t <- s5t |>
  dplyr::mutate(
    Salience  = dplyr::if_else(stringr::str_starts(taskCondition, "high"), "High", "Low"),
    Direction = dplyr::if_else(stringr::str_ends(taskCondition,   "Acc"),  "Faster", "Slower")
  )

# Study 5: session-mean Confidence and Awareness across sessions
s5s <- s5s |>
  dplyr::mutate(
    mean_Confidence = rowMeans(
      dplyr::across(c(mean_Confidence_ses1, mean_Confidence_ses2)), na.rm = TRUE),
    Awareness = rowMeans(
      dplyr::across(c(Awareness_ses1, Awareness_ses2)), na.rm = TRUE)
  )

# Convenience subsets used across multiple analysis files
s5_long_breath <- dplyr::filter(s5l, Condition == "breath")

# Pre-sorted Study 1A for MRC threshold computation
s1l_A_sorted <- s1l |>
  dplyr::filter(Group == "TaskA") |>
  dplyr::arrange(id, TrialNum)

message("Data ready.")


# ── PRIMARY RESULTS ───────────────────────────────────────────

# Task Validation: Change² dose-response across all studies (main text Table 2)
# Creates: table_detection_change2.csv
# Creates env objects: s{N}_det — used by analysis_val_thresholds.R
source(paste0(ANALYSIS_DIR, "analysis_val_detection.R"))

# Task Validation: pilot study comparisons and staircase convergence (Supplement S1.1–S1.3)
# Creates: study1_task_comparison.csv, table_study3_salience_accuracy.csv,
#          table_staircase_convergence.csv, study2_convergence_elbow.csv
source(paste0(ANALYSIS_DIR, "analysis_val_pilot_studies.R"))

# Task Validation: thresholds, d', ICC (Supplement S1.4)
# NOTE: requires analysis_val_detection.R to have run first
#       (uses s{N}_det objects for table_validation.csv assembly)
# Creates: table_validation.csv, table_test_dprime.csv, table_reliability.csv
# Creates env objects: s{N}_thresh, s{N}_conf, s{N}_maia — used by analysis_maia.R
source(paste0(ANALYSIS_DIR, "analysis_val_thresholds.R"))

# Awareness Gates Arousal Transfer (H4A, H4B, H4C)
# Creates: table_arousal.csv, barrett_tce_disambiguation.csv,
#          meta_h4b_pooled.csv, table_belt_physio_arousal.csv
# Creates env objects: s{N}_arousal — used by analysis_maia.R
source(paste0(ANALYSIS_DIR, "analysis_arousal.R"))

# Bayesian null test: missed-change trials vs. no-change baseline
# BF01 values reported in main text (Studies 1A, 2, 4, 5)
# Creates: miss_baseline_bf.csv
source(paste0(ANALYSIS_DIR, "analysis_miss_baseline.R"))

# Study 3 misattribution chain: Change -> Arousal -> Attraction
# Creates: table_mediation.csv
source(paste0(ANALYSIS_DIR, "analysis_study3_attraction_mediation.R"))

# MAIA: sensibility vs. sensitivity (H3A, H3B)
# NOTE: requires analysis_val_thresholds.R to have run first
#       (uses s{N}_maia, s{N}_thresh, s{N}_conf objects)
# Creates: table_maia.csv
source(paste0(ANALYSIS_DIR, "analysis_maia.R"))


# ── SUPPLEMENTARY ─────────────────────────────────────────────

# S2: TCE sensitivity analyses
source(paste0(ANALYSIS_DIR, "analysis_tce.R"))

# S3: Individual differences (Studies 4 and 5 replication)
source(paste0(ANALYSIS_DIR, "analysis_individual_differences.R"))

# S6: Belt entrainment and interoceptive contribution to detection
source(paste0(ANALYSIS_DIR, "analysis_belt.R"))
source(paste0(ANALYSIS_DIR, "belt_salience_followup.R"))
source(paste0(ANALYSIS_DIR, "analysis_s6_entrainment.R"))

# Exploratory Study 5 MAIA and threshold breakdown
source(paste0(ANALYSIS_DIR, "analysis_study5_exploratory.R"))

# Controls for Global Self Esteem on MAIA in Study 5
source(paste0(ANALYSIS_DIR, "analysis_s8_maia_selfesteem.R")) 

# HBD cardiac interoception (exploratory)
source(paste0(ANALYSIS_DIR, "analysis_hbd.R"))

# ── Zip all results ───────────────────────────────────────────
result_files <- list.files(RESULTS_DIR, pattern = "\\.csv$", full.names = TRUE)
zip(zipfile = file.path(RESULTS_DIR, "all_results.zip"), files = result_files)
message("Zipped ", length(result_files), " CSV files to all_results.zip")

message("\nMainAnalysis.R complete.")

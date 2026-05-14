# ============================================================
# tables_format.R
# BCAT Paper — APA 7th Edition Table Formatter
#
# Pure formatting script. Reads authoritative CSVs from RESULTS_DIR.
# Runs NO models. Fails loudly if any source file is missing.
#
# Output: tables_main.docx  (Tables 2–3, main text)
#         tables_supplement.docx  (Supplementary Tables S1–S5)
#
# Run after MainAnalysis.R has completed and all CSVs are present.
# ============================================================

# ── Packages ──────────────────────────────────────────────────
packages <- c("tidyverse", "flextable", "officer")
new_packages <- packages[!sapply(packages, requireNamespace, quietly = TRUE)]
if (length(new_packages)) install.packages(new_packages)
options(readr.show_col_types = FALSE)
for (thispack in packages) {
  library(thispack, character.only = TRUE, quietly = TRUE, verbose = FALSE)
}

# ── Paths ──────────────────────────────────────────────────────
RESULTS_DIR <- "I:/Shared drives/Interoception 2025/Paper/Results/"

# Helper: load a CSV and stop with a clear message if missing
load_csv <- function(filename) {
  path <- file.path(RESULTS_DIR, filename)
  if (!file.exists(path))
    stop(sprintf(
      "Source file not found: %s\nRun MainAnalysis.R first.", path))
  readr::read_csv(path, show_col_types = FALSE)
}


# ============================================================
# FORMATTING HELPERS
# All number-formatting decisions live here.
# ============================================================

# p-value: APA 7 style — no leading zero, 3 dp, "< .001" floor
fmt_p <- function(p) {
  dplyr::case_when(
    is.na(p)   ~ "",
    p < .001   ~ "< .001",
    p < .01    ~ paste0("= ", sub("^0", "", formatC(p, digits = 3, format = "f"))),
    TRUE       ~ paste0("= ", sub("^0", "", formatC(p, digits = 3, format = "f")))
  )
}

# Correlation / partial r: no leading zero, signed, 2 dp
fmt_r <- function(r, digits = 2) {
  ifelse(is.na(r), "",
         sub("^(-?)0", "\\1",
             formatC(round(r, digits), digits = digits, format = "f")))
}

# 95% CI from lower/upper: "[.xx, .xx]"
fmt_ci <- function(lo, hi, digits = 2) {
  ifelse(is.na(lo) | is.na(hi), "",
         sprintf("[%s, %s]", fmt_r(lo, digits), fmt_r(hi, digits)))
}

# b and SE combined: "−5.38 (0.96)" — uses Unicode minus for negative
fmt_b_se <- function(b, se, digits = 2) {
  ifelse(is.na(b) | is.na(se), "",
         sprintf("%s (%s)",
                 formatC(round(b, digits), digits = digits, format = "f"),
                 formatC(round(se, digits), digits = digits, format = "f")))
}

# chi-squared with df: "680.2(4)"
fmt_chi2_df <- function(chi2, df, digits = 1) {
  ifelse(is.na(chi2), "",
         sprintf("%s(%s)",
                 formatC(round(chi2, digits), digits = digits, format = "f"),
                 as.integer(round(df))))
}

# BF01: round sensibly — 1 dp up to 10, integer above
fmt_bf <- function(bf) {
  dplyr::case_when(
    is.na(bf)  ~ "",
    bf >= 100  ~ formatC(round(bf), format = "d", big.mark = ","),
    bf >= 10   ~ formatC(round(bf, 0), digits = 0, format = "f"),
    TRUE       ~ formatC(round(bf, 1), digits = 1, format = "f")
  )
}

# Pretty study labels
fmt_study <- function(x) {
  dplyr::recode(x,
                Study1A = "Study 1A", Study2 = "Study 2",
                Study3  = "Study 3",  Study4  = "Study 4",
                Study5  = "Study 5",  Study1B = "Study 1B")
}


# ============================================================
# APA THEME
# Single function applied to every flextable in the script.
# Change font / size / border width here and it propagates.
# ============================================================

apa_theme <- function(ft, note_text = NULL) {
  # Typography
  ft <- flextable::font(ft, fontname = "Times New Roman", part = "all")
  ft <- flextable::fontsize(ft, size = 11, part = "all")
  ft <- flextable::fontsize(ft, size = 11, part = "header")
  
  # Remove all borders, then add only the three APA lines
  ft <- flextable::border_remove(ft)
  thick <- officer::fp_border(width = 1.5, color = "black")
  thin  <- officer::fp_border(width = 0.5, color = "black")
  
  ft <- flextable::hline_top(ft, border = thick, part = "header")
  ft <- flextable::hline_bottom(ft, border = thin,  part = "header")
  ft <- flextable::hline_bottom(ft, border = thick, part = "body")
  
  # Alignment
  ft <- flextable::align(ft, align = "left",   part = "all", j = 1)
  ft <- flextable::align(ft, align = "center", part = "header")
  ft <- flextable::align(ft, align = "center", part = "body",   j = -1)
  
  # Header italic
  ft <- flextable::italic(ft, part = "header")
  
  # Note (footer)
  if (!is.null(note_text)) {
    ft <- flextable::add_footer_lines(ft, values = note_text)
    ft <- flextable::font(ft, fontname = "Times New Roman", part = "footer")
    ft <- flextable::fontsize(ft, size = 10, part = "footer")
    ft <- flextable::italic(ft, part = "footer", j = 1)
    ft <- flextable::align(ft, align = "left", part = "footer")
  }
  
  # Padding
  ft <- flextable::padding(ft, padding = 3, part = "all")
  
  ft
}


# ============================================================
# TABLE 2: AROUSAL TRANSFER (H4A–H4C)
# Sources: table_arousal.csv, meta_h4b_pooled.csv
# ============================================================

make_table2 <- function() {
  
  raw   <- load_csv("table_arousal.csv")
  meta  <- load_csv("meta_h4b_pooled.csv")
  
  # ── Format display columns ────────────────────────────────
  d <- raw |>
    dplyr::mutate(
      Study        = fmt_study(study),
      N            = as.integer(n),
      `chi2(df)`   = fmt_chi2_df(H4A_chi2, H4A_df),
      `p_H4A`      = fmt_p(H4A_p_LRT),
      `b_se_H4B`   = fmt_b_se(H4B_b, H4B_SE),
      `r_H4B`      = fmt_r(H4B_partial_r),
      `p_H4B`      = fmt_p(H4B_p),
      `b_se_H4C`   = fmt_b_se(H4C_b, H4C_SE),
      `r_H4C`      = fmt_r(H4C_partial_r),
      `p_H4C`      = fmt_p(H4C_p)
    ) |>
    dplyr::select(Study, N, `chi2(df)`, p_H4A,
                  b_se_H4B, r_H4B, p_H4B,
                  b_se_H4C, r_H4C, p_H4C)
  
  # ── Meta-analysis note text ────────────────────────────────
  m <- meta[1, ]
  meta_note <- sprintf(
    paste0("Pooled H4B (random-effects meta-analysis, k = %d): ",
           "r = %s, 95%% CI [%s, %s], p %s, I\u00b2 = %.1f%%."),
    as.integer(m$k_studies),
    fmt_r(m$r_pooled),
    fmt_r(m$r_lower),
    fmt_r(m$r_upper),
    fmt_p(m$p_value),
    m$I2_pct)
  
  note <- paste0(
    "Note. H4A = likelihood-ratio test of quadratic Change polynomial on Arousal (df = ",
    "degrees of freedom for quadratic term vs. intercept-only model). ",
    "H4B = Change \u00d7 Accuracy interaction; b and SE are unstandardised LMM coefficients; ",
    "partial r = t / \u221a(t\u00b2 + df). ",
    "H4C = Change \u00d7 Condition interaction (interoceptive specificity; ",
    "Studies 4\u20135 only; breath vs. visual pacing). ",
    meta_note)
  
  # ── Build flextable ────────────────────────────────────────
  ft <- flextable::flextable(d)
  
  # Rename column headers (italic symbols added via compose below)
  ft <- flextable::set_header_labels(ft,
                                     Study      = "Study",
                                     N          = "N",
                                     `chi2(df)` = "\u03c7\u00b2(df)",   # χ²(df)
                                     p_H4A      = "p",
                                     b_se_H4B   = "b (SE)",
                                     r_H4B      = "partial r",
                                     p_H4B      = "p",
                                     b_se_H4C   = "b (SE)",
                                     r_H4C      = "partial r",
                                     p_H4C      = "p")
  
  # Spanning header row
  ft <- flextable::add_header_row(ft,
                                  values     = c("", "",
                                                 "H4A: Change effect",
                                                 "H4B: Awareness gating",
                                                 "H4C: Interoceptive specificity"),
                                  colwidths  = c(1, 1, 2, 3, 3))
  
  # Merge blank spans in top header
  ft <- flextable::merge_h(ft, part = "header")
  ft <- flextable::align(ft, align = "center", part = "header")
  
  # Column widths (inches; total = 6.5)
  ft <- flextable::width(ft, j = 1,  width = 0.70)  # Study
  ft <- flextable::width(ft, j = 2,  width = 0.35)  # N
  ft <- flextable::width(ft, j = 3,  width = 0.85)  # chi2(df)
  ft <- flextable::width(ft, j = 4,  width = 0.50)  # p H4A
  ft <- flextable::width(ft, j = 5,  width = 0.90)  # b(SE) H4B
  ft <- flextable::width(ft, j = 6,  width = 0.55)  # partial r H4B
  ft <- flextable::width(ft, j = 7,  width = 0.50)  # p H4B
  ft <- flextable::width(ft, j = 8,  width = 0.90)  # b(SE) H4C
  ft <- flextable::width(ft, j = 9,  width = 0.55)  # partial r H4C
  ft <- flextable::width(ft, j = 10, width = 0.50)  # p H4C
  
  ft <- apa_theme(ft, note_text = note)
  ft
}


# ============================================================
# TABLE 3: MAIA DISSOCIATION (H3A–H3B)
# Sources: table_maia.csv, meta_h3_maia_dissociation.csv
# ============================================================

make_table3 <- function() {
  
  raw  <- load_csv("table_maia.csv")
  meta <- load_csv("meta_h3_maia_dissociation.csv")
  
  # ── Per-study rows ─────────────────────────────────────────
  d <- raw |>
    dplyr::mutate(
      Study        = fmt_study(study),
      N            = as.integer(n),
      r_H3A        = fmt_r(H3A_r),
      CI_H3A       = fmt_ci(H3A_CI_lower, H3A_CI_upper),
      p_H3A        = fmt_p(H3A_p),
      r_H3B        = fmt_r(H3B_r),
      CI_H3B       = fmt_ci(H3B_CI_lower, H3B_CI_upper),
      p_H3B        = fmt_p(H3B_p),
      BF01         = fmt_bf(H3B_BF01)
    ) |>
    # Study 3: mark with footnote marker; BF01 not applicable
    dplyr::mutate(
      Study = dplyr::if_else(study == "Study3",
                             paste0(Study, "\u1d43"),  # superscript a
                             Study)
    ) |>
    dplyr::select(Study, N, r_H3A, CI_H3A, p_H3A, r_H3B, CI_H3B, p_H3B, BF01)
  
  # ── Pooled row ─────────────────────────────────────────────
  h3a <- meta |> dplyr::filter(grepl("H3A|Confidence", Contrast))
  h3b <- meta |> dplyr::filter(grepl("H3B|Threshold",  Contrast))
  
  pooled_n <- sum(raw$n[raw$study != "Study3"])
  
  pooled_row <- tibble::tibble(
    Study  = "Pooled (k = 4)",
    N      = as.integer(pooled_n),
    r_H3A  = fmt_r(h3a$r_pooled),
    CI_H3A = fmt_ci(h3a$r_lower, h3a$r_upper),
    p_H3A  = "",   # pulled from meta_h3 p — add if available
    r_H3B  = fmt_r(h3b$r_pooled),
    CI_H3B = fmt_ci(h3b$r_lower, h3b$r_upper),
    p_H3B  = "",
    BF01   = "\u2014"
  )
  
  d_full <- dplyr::bind_rows(d, pooled_row)
  
  # ── Note ───────────────────────────────────────────────────
  note <- paste0(
    "Note. H3A = zero-order Pearson r between MAIA total score and ",
    "mean trial-level detection confidence (person-level). ",
    "H3B = Pearson r between MAIA total score and mean detection threshold ",
    "(person-level; mean |Change| on staircase trials used as threshold proxy). ",
    "BF\u2080\u2081 = Bayes factor favouring the null (JZS prior, r = 0.707); ",
    "values > 3 indicate moderate evidence for H\u2080. ",
    "Pooled H3A: all 5 studies; Pooled H3B: k = 4, Study 3 excluded ",
    "(mean accuracy used as proxy; not comparable with staircase thresholds). ",
    "\u1d43Study 3 used fixed change magnitudes; H3B reports r(MAIA, mean accuracy) ",
    "rather than r(MAIA, threshold). BF\u2080\u2081 = 0.85 for Study 3 H3B indicates ",
    "inconclusive evidence; negative direction is anomalous relative to other studies.")
  
  # ── Build flextable ────────────────────────────────────────
  ft <- flextable::flextable(d_full)
  
  ft <- flextable::set_header_labels(ft,
                                     Study  = "Study",
                                     N      = "N",
                                     r_H3A  = "r",
                                     CI_H3A = "95% CI",
                                     p_H3A  = "p",
                                     r_H3B  = "r",
                                     CI_H3B = "95% CI",
                                     p_H3B  = "p",
                                     BF01   = "BF\u2080\u2081")
  
  ft <- flextable::add_header_row(ft,
                                  values    = c("", "",
                                                "H3A: MAIA \u2192 Confidence",
                                                "H3B: MAIA \u2192 Threshold"),
                                  colwidths = c(1, 1, 3, 4))
  
  ft <- flextable::merge_h(ft, part = "header")
  ft <- flextable::align(ft, align = "center", part = "header")
  
  # Bold the pooled row
  ft <- flextable::bold(ft, i = nrow(d_full), part = "body")
  
  # Horizontal rule above pooled row
  ft <- flextable::hline(ft,
                         i      = nrow(d_full) - 1,
                         border = officer::fp_border(width = 0.5, color = "black"),
                         part   = "body")
  
  # Column widths (total ≈ 6.3 inches)
  ft <- flextable::width(ft, j = 1, width = 0.85)  # Study
  ft <- flextable::width(ft, j = 2, width = 0.35)  # N
  ft <- flextable::width(ft, j = 3, width = 0.50)  # r H3A
  ft <- flextable::width(ft, j = 4, width = 0.90)  # CI H3A
  ft <- flextable::width(ft, j = 5, width = 0.45)  # p H3A
  ft <- flextable::width(ft, j = 6, width = 0.50)  # r H3B
  ft <- flextable::width(ft, j = 7, width = 0.90)  # CI H3B
  ft <- flextable::width(ft, j = 8, width = 0.45)  # p H3B
  ft <- flextable::width(ft, j = 9, width = 0.55)  # BF01
  
  ft <- apa_theme(ft, note_text = note)
  ft
}


# ============================================================
# TABLE 1: STUDY OVERVIEW
# Hardcoded — no source CSV. All values from summary data files
# and methods section. Study 1B merged with 1A via footnote.
# ============================================================

make_table1 <- function() {
  
  yes  <- "\u2713"   # ✓
  no   <- "\u2014"   # —
  
  d <- tibble::tibble(
    Feature = c(
      "N",
      "Age, M (SD)",
      "Women / Men / Other",
      "Setting",
      "Recruitment",
      "Staircase",
      "Arousal scale",
      "Salience manipulation",
      "Visual control (H4C)",
      "Physiological recording",
      "Preregistered"
    ),
    Study1A = c(
      "181",
      "25.7 (8.4)",
      "60 / 113",
      "Online",
      "Prolific",
      "Robbins-Monro",
      "VAS (0\u201350)",
      no, no, no, no
    ),
    Study2 = c(
      "166",
      "28.1 (10.3)",
      "51 / 114",
      "Online",
      "Prolific",
      "Robbins-Monro",
      "VAS (0\u201350)",
      no, no, no, no
    ),
    Study3 = c(
      "103",
      "19.5 (2.0)",
      "76 / 27",
      "Lab",
      "UTM",
      "Fixed magnitudes",
      "SAM",
      yes, no, no, no
    ),
    Study4 = c(
      "131",
      "19.4 (3.4)",
      "92 / 36 / 2",
      "Online",
      "UTM SONA",
      "Quest",
      "Emoji (1\u20136)",
      yes, yes, no, no
    ),
    Study5 = c(
      "206",
      "19.1 (2.1)",
      "162 / 35 / 4",
      "Lab",
      "UTM SONA",
      "Quest",
      "Emoji (1\u20136)",
      yes, yes, yes, yes
    )
  )
  
  note <- paste0(
    "Note. UTM = University of Toronto Mississauga. ",
    "VAS = visual analog scale. SAM = Self-Assessment Manikin. ",
    "Quest = Watson-Pelli adaptive staircase (75% correct target). ",
    "Robbins-Monro = stochastic approximation staircase. ",
    "Salience manipulation = high (abrupt) vs. low (gradual) onset. ",
    "Visual control = between-groups visual pacing condition (H4C). ",
    "\u1d43Study 1B was conducted in the same session as Study 1A using an ascending-limits ",
    "procedure (N = 181). Study 1B data are used for procedure comparison only ",
    "(Supplementary S1.1) and are excluded from all arousal and MAIA analyses."
  )
  
  ft <- flextable::flextable(d)
  
  # Rename columns — Unicode superscript safe here (not in backtick names)
  ft <- flextable::set_header_labels(ft,
                                     Feature = "",
                                     Study1A = "Study 1A/1B\u1d43",
                                     Study2  = "Study 2",
                                     Study3  = "Study 3",
                                     Study4  = "Study 4",
                                     Study5  = "Study 5"
  )
  
  # Bold the N row
  ft <- flextable::bold(ft, i = 1, part = "body")
  
  # Left-align feature column, center study columns
  ft <- flextable::align(ft, j = 1, align = "left",   part = "all")
  ft <- flextable::align(ft, j = -1, align = "center", part = "all")
  
  # Column widths (total = 6.5")
  ft <- flextable::width(ft, j = 1, width = 1.60)   # Feature label
  ft <- flextable::width(ft, j = 2, width = 0.98)   # Study 1A/1B
  ft <- flextable::width(ft, j = 3, width = 0.88)   # Study 2
  ft <- flextable::width(ft, j = 4, width = 0.88)   # Study 3
  ft <- flextable::width(ft, j = 5, width = 0.88)   # Study 4
  ft <- flextable::width(ft, j = 6, width = 0.88)   # Study 5
  
  # Horizontal rule separating demographics from design features
  ft <- flextable::hline(ft,
                         i      = 3,
                         border = officer::fp_border(width = 0.5, color = "black"),
                         part   = "body")
  
  ft <- apa_theme(ft, note_text = note)
  ft
}


# ============================================================
# SUPPLEMENTARY TABLES
# Each builder reads its source CSV and returns a flextable.
# Add to the supplement docx section below as they are built.
# ============================================================

# ── S1: Task Validation (H1, H2, H5) ─────────────────────────
make_table_s1 <- function() {
  raw <- load_csv("table_validation.csv")
  
  d <- raw |>
    dplyr::mutate(
      Study      = fmt_study(study),
      `H1 b(SE)` = fmt_b_se(H1_b, H1_SE),
      `H1 pr`    = fmt_r(H1_partial_r),
      `H1 p`     = fmt_p(H1_p),
      `H2 b(SE)` = fmt_b_se(H2_b, H2_SE),
      `H2 pr`    = fmt_r(H2_partial_r),
      `H2 p`     = fmt_p(H2_p),
      `H5 b(SE)` = fmt_b_se(H5_b, H5_SE),
      `H5 pr`    = fmt_r(H5_partial_r),
      `H5 p`     = fmt_p(H5_p)
    ) |>
    dplyr::select(Study,
                  `H1 b(SE)`, `H1 pr`, `H1 p`,
                  `H2 b(SE)`, `H2 pr`, `H2 p`,
                  `H5 b(SE)`, `H5 pr`, `H5 p`)
  
  note <- paste0(
    "Note. H1 = direction effect on detection threshold (Slower vs. Faster). ",
    "H2 = salience effect on detection threshold (High vs. Low). ",
    "H5 = staircase-to-test predictive validity (logistic regression). ",
    "b = unstandardised coefficient; partial r = effect size. ",
    "Cells are empty where the hypothesis was not tested in that study.")
  
  ft <- flextable::flextable(d) |>
    flextable::add_header_row(
      values    = c("", "H1: Direction", "H2: Salience", "H5: Test validity"),
      colwidths = c(1, 3, 3, 3)) |>
    flextable::merge_h(part = "header") |>
    flextable::align(align = "center", part = "header") |>
    apa_theme(note_text = note)
  
  ft
}

# ── S2: Test-block 3AFC d' (H5) ──────────────────────────────
make_table_s2 <- function() {
  raw <- load_csv("table_test_dprime.csv")
  
  d <- raw |>
    dplyr::mutate(
      Study     = dplyr::recode(study,
                                Study4 = "Study 4", Study5 = "Study 5",
                                Study5_Visual = "Study 5 (visual)"),
      Group     = group,
      Salience  = salience,
      `N trials` = n_trials,
      `n ppts`  = n_participants,
      Pc        = formatC(round(Pc, 3), digits = 3, format = "f"),
      `d' (3AFC)` = formatC(round(dprime_3afc, 2), digits = 2, format = "f")
    ) |>
    dplyr::select(Study, Group, Salience, `N trials`, `n ppts`, Pc, `d' (3AFC)`)
  
  note <- paste0(
    "Note. d' computed by numerical inversion of the 3AFC Pc function ",
    "(integral of normal over unit square). ",
    "Quest staircase target: d' = 1.5 (Pc \u2248 .75) at high salience.")
  
  ft <- flextable::flextable(d) |>
    apa_theme(note_text = note)
  
  ft
}

# ── S3: Test-retest Reliability (H6, Study 5) ────────────────
make_table_s3 <- function() {
  raw <- load_csv("table_reliability.csv")
  
  d <- raw |>
    dplyr::mutate(
      Condition = gsub("_", " \u00d7 ", condition),
      Group     = group,
      n         = as.integer(n),
      ICC       = formatC(round(icc, 2),       digits = 2, format = "f"),
      `95% CI`  = fmt_ci(icc_lower, icc_upper)
    ) |>
    dplyr::select(Condition, Group, n, ICC, `95% CI`)
  
  note <- paste0(
    "Note. Two-way agreement ICC (single measures). ",
    "Breath-first group: both sessions used breath-paced stimuli (breath\u2013breath). ",
    "Visual-first group: Session 1 = visual-paced, Session 2 = breath-paced; ",
    "ICC indexes cross-condition divergent validity rather than test-retest reliability. ",
    "Pre-registered criterion: ICC \u2265 .70.")
  
  ft <- flextable::flextable(d) |>
    apa_theme(note_text = note)
  
  ft
}

# ── S4: Staircase Convergence ─────────────────────────────────
make_table_s4 <- function() {
  raw <- load_csv("table_staircase_convergence.csv")
  
  d <- raw |>
    dplyr::mutate(
      Study     = fmt_study(study),
      Condition = gsub("x", " \u00d7 ", cell),
      n         = as.integer(n),
      `Mean trials`  = formatC(round(n_trials_mean, 1), digits = 1, format = "f"),
      `SD first 6`   = formatC(round(SD_first6, 3), digits = 3, format = "f"),
      `SD last 6`    = formatC(round(SD_last6,  3), digits = 3, format = "f"),
      `% reduction`  = formatC(round(pct_reduction, 1), digits = 1, format = "f"),
      `dz`           = formatC(round(cohens_dz, 2), digits = 2, format = "f"),
      p              = fmt_p(p)
    ) |>
    dplyr::select(Study, Condition, n, `Mean trials`,
                  `SD first 6`, `SD last 6`, `% reduction`, dz, p)
  
  note <- paste0(
    "Note. SD reduction tests whether trial-to-trial variability in Change magnitude ",
    "decreases across the staircase (first 6 vs. last 6 trials; paired t-test). ",
    "dz = Cohen\u2019s dz.")
  
  ft <- flextable::flextable(d) |>
    apa_theme(note_text = note)
  
  ft
}


# ============================================================
# BUILD AND SAVE
# ============================================================

message("Building Table 1 (Study Overview)...")
ft1 <- make_table1()

message("Building Table 2 (Arousal Transfer)...")
ft2 <- make_table2()

message("Building Table 3 (MAIA Dissociation)...")
ft3 <- make_table3()

message("Building supplementary tables...")
ft_s1 <- make_table_s1()
ft_s2 <- make_table_s2()
ft_s3 <- make_table_s3()
ft_s4 <- make_table_s4()

# ── Main tables docx ──────────────────────────────────────────
main_path <- file.path(RESULTS_DIR, "tables_main.docx")

doc_main <- officer::read_docx() |>
  officer::body_add_par("Table 1", style = "heading 2") |>
  officer::body_add_par(
    "Study Overview and Sample Characteristics",
    style = "Normal") |>
  officer::body_add_par("", style = "Normal") |>
  flextable::body_add_flextable(ft1) |>
  officer::body_add_break() |>
  officer::body_add_par("Table 2", style = "heading 2") |>
  officer::body_add_par(
    "Awareness Gates Arousal Transfer: Cross-Study Summary (H4A\u2013H4C)",
    style = "Normal") |>
  officer::body_add_par("", style = "Normal") |>
  flextable::body_add_flextable(ft2) |>
  officer::body_add_break() |>
  officer::body_add_par("Table 3", style = "heading 2") |>
  officer::body_add_par(
    "MAIA Predicts Detection Confidence but Not Objective Threshold (H3A\u2013H3B)",
    style = "Normal") |>
  officer::body_add_par("", style = "Normal") |>
  flextable::body_add_flextable(ft3)

print(doc_main, target = main_path)
message("Saved: tables_main.docx")

# ── Supplement tables docx ────────────────────────────────────
supp_path <- file.path(RESULTS_DIR, "tables_supplement.docx")

doc_supp <- officer::read_docx() |>
  officer::body_add_par("Table S1", style = "heading 2") |>
  officer::body_add_par(
    "Task Validation: Direction (H1), Salience (H2), and Predictive Validity (H5)",
    style = "Normal") |>
  officer::body_add_par("", style = "Normal") |>
  flextable::body_add_flextable(ft_s1) |>
  officer::body_add_break() |>
  officer::body_add_par("Table S2", style = "heading 2") |>
  officer::body_add_par(
    "Test-Block 3AFC d' by Study and Salience (H5)",
    style = "Normal") |>
  officer::body_add_par("", style = "Normal") |>
  flextable::body_add_flextable(ft_s2) |>
  officer::body_add_break() |>
  officer::body_add_par("Table S3", style = "heading 2") |>
  officer::body_add_par(
    "Test-Retest Reliability of Staircase Threshold Estimates (H6, Study 5)",
    style = "Normal") |>
  officer::body_add_par("", style = "Normal") |>
  flextable::body_add_flextable(ft_s3) |>
  officer::body_add_break() |>
  officer::body_add_par("Table S4", style = "heading 2") |>
  officer::body_add_par(
    "Staircase Convergence: Trial-to-Trial Variability Reduction",
    style = "Normal") |>
  officer::body_add_par("", style = "Normal") |>
  flextable::body_add_flextable(ft_s4)

print(doc_supp, target = supp_path)
message("Saved: tables_supplement.docx")

message("\ntables_format.R complete.")
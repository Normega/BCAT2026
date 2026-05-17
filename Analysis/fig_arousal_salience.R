# fig_arousal_salience.R
# Arousal ~ Change, split by Accuracy x Salience
# Layout mirrors fig_replication.R: 3 columns x 2 rows
#   Row 1: Study 1 | Study 2 | Study 3*
#   Row 2: Study 4 | Study 5 | Forest plot (H4B Change x Accuracy partial r)
#
# Studies 1 and 2: 2 lines (Accuracy only; no salience manipulation)
# Studies 3, 4, 5: 4 lines (Accuracy x Salience)
#   Colour  -> Accuracy:  orange = Detected, blue = Missed
#   Linetype -> Salience: solid  = High,     dashed = Low

# Set Up ---------
## Load libraries ---------
packages <- c("tidyverse", "lme4", "lmerTest", "ggeffects", "patchwork")
new_packages <- packages[!sapply(packages, requireNamespace, quietly = TRUE)]
if (length(new_packages)) install.packages(new_packages)
options(readr.show_col_types = FALSE)
for (thispack in packages) {
  library(thispack, character.only = TRUE, quietly = TRUE, verbose = FALSE)
}

DDIR    <- file.path(MAIN_DIR,"Data")
FIG_DIR <- file.path(MAIN_DIR,"Figures")
ctrl    <- lmerControl(optimizer = "bobyqa")

# ── Colour / linetype palette ─────────────────────────────────────────────────
col_detected <- "#E69F00"
col_missed   <- "#0072B2"

acc_cols   <- c("0" = col_missed,   "1" = col_detected)
acc_labels <- c("0" = "Missed",     "1" = "Detected")
sal_types  <- c("High" = "solid",   "Low" = "dashed")
sal_labels <- c("High" = "High salience", "Low" = "Low salience")

# ── Shared theme ──────────────────────────────────────────────────────────────
theme_fig <- function(show_legend = FALSE) {
  theme_minimal(base_size = 11) +
    theme(
      plot.title       = element_text(face = "bold", size = 11),
      plot.subtitle    = element_text(size = 9, colour = "grey40"),
      panel.grid.minor = element_blank(),
      legend.position  = if (show_legend) "bottom" else "none"
    )
}

# ── Panel builder: 2 lines (Accuracy only; Studies 1-2) ──────────────────────
make_panel_2 <- function(df, title, subtitle = NULL,
                          show_y = TRUE,
                          x_breaks = c(-0.5, 0, 0.5),
                          x_labels = c("-0.5", "0", "0.5")) {
  df$Arousal_z <- as.numeric(scale(df$Arousal))

  m <- tryCatch(
    lmer(Arousal_z ~ Accuracy * poly(Change, 2) + (Change | id),
         data = df, control = ctrl),
    error = function(e)
      lmer(Arousal_z ~ Accuracy * poly(Change, 2) + (1 | id),
           data = df, control = ctrl)
  )
  if (isSingular(m))
    m <- lmer(Arousal_z ~ Accuracy * poly(Change, 2) + (1 | id),
              data = df, control = ctrl)

  pred <- ggeffects::ggpredict(m, terms = c("Change [all]", "Accuracy [0,1]"))

  ggplot(pred, aes(x = x, y = predicted,
                   colour = group, fill = group)) +
    geom_ribbon(aes(ymin = conf.low, ymax = conf.high),
                alpha = 0.20, colour = NA) +
    geom_line(linewidth = 1) +
    scale_colour_manual(values = acc_cols, labels = acc_labels,
                        name = "Detection") +
    scale_fill_manual(values = acc_cols, labels = acc_labels,
                      name = "Detection") +
    scale_x_continuous(breaks = x_breaks, labels = x_labels) +
    labs(x        = "Breathing rate change",
         y        = if (show_y) "Predicted arousal (standardised)" else NULL,
         title    = title,
         subtitle = subtitle) +
    theme_fig() +
    theme(axis.title.y = if (show_y) element_text() else element_blank())
}

# ── Panel builder: 4 lines (Accuracy x Salience; Studies 3-5) ────────────────
make_panel_4 <- function(df, title, subtitle = NULL,
                          show_y = TRUE, show_legend = FALSE,
                          x_breaks = c(-0.5, 0, 0.5),
                          x_labels = c("-0.5", "0", "0.5")) {
  df <- df |>
    dplyr::filter(!is.na(Salience)) |>
    dplyr::mutate(
      Arousal_z = as.numeric(scale(Arousal)),
      Salience  = factor(Salience, levels = c("High", "Low"))
    )

  m <- tryCatch(
    lmer(Arousal_z ~ Accuracy * Salience * poly(Change, 2) + (1 | id),
         data = df, control = ctrl),
    error = function(e)
      lmer(Arousal_z ~ Accuracy * Salience + poly(Change, 2) + (1 | id),
           data = df, control = ctrl)
  )
  if (isSingular(m))
    m <- lmer(Arousal_z ~ Accuracy * Salience * poly(Change, 2) + (1 | id),
              data = df, control = ctrl,
              REML = FALSE)

  pred <- ggeffects::ggpredict(
    m, terms = c("Change [all]", "Accuracy [0,1]", "Salience [High,Low]")
  )
  # ggpredict returns: x, predicted, group (Accuracy), facet (Salience)
  pred_df <- as.data.frame(pred) |>
    dplyr::rename(Accuracy = group, Salience = facet) |>
    dplyr::mutate(
      Accuracy = as.character(Accuracy),
      Salience = factor(Salience, levels = c("High", "Low"))
    )

  ggplot(pred_df,
         aes(x        = x,
             y        = predicted,
             colour   = Accuracy,
             fill     = Accuracy,
             linetype = Salience)) +
    geom_ribbon(aes(ymin = conf.low, ymax = conf.high),
                alpha = 0.15, colour = NA) +
    geom_line(linewidth = 1) +
    scale_colour_manual(values = acc_cols, labels = acc_labels,
                        name = "Detection") +
    scale_fill_manual(values = acc_cols, labels = acc_labels,
                      name = "Detection") +
    scale_linetype_manual(values = sal_types, labels = sal_labels,
                          name = "Salience") +
    scale_x_continuous(breaks = x_breaks, labels = x_labels) +
    labs(x        = "Breathing rate change",
         y        = if (show_y) "Predicted arousal (standardised)" else NULL,
         title    = title,
         subtitle = subtitle) +
    theme_fig(show_legend = show_legend) +
    theme(axis.title.y = if (show_y) element_text() else element_blank())
}

# ── Load data ─────────────────────────────────────────────────────────────────
s1l <- readr::read_csv(file.path(DDIR, "study1_long.csv"))
s2l <- readr::read_csv(file.path(DDIR, "study2_long.csv"))
s3l <- readr::read_csv(file.path(DDIR, "study3_long.csv"))
s4l <- readr::read_csv(file.path(DDIR, "study4_long.csv"))
s5l <- readr::read_csv(file.path(DDIR, "study5_long.csv")) |>
  dplyr::filter(Condition == "breath")

# ── Build panels ──────────────────────────────────────────────────────────────
p1 <- make_panel_2(s1l,
                   title    = "Study 1",
                   subtitle = "Online  |  N = 181",
                   show_y   = TRUE)

p2 <- make_panel_2(s2l,
                   title    = "Study 2",
                   subtitle = "Online  |  N = 166",
                   show_y   = FALSE)

p3 <- make_panel_4(s3l,
                   title    = "Study 3 *",
                   subtitle = "Lab  |  N = 103  |  Fixed magnitudes",
                   show_y   = FALSE,
                   x_breaks = c(-0.65, 0, 0.65),
                   x_labels = c("-0.65", "0", "0.65"))

p4 <- make_panel_4(s4l,
                   title    = "Study 4",
                   subtitle = "Online  |  N = 131",
                   show_y   = TRUE)

p5 <- make_panel_4(s5l,
                   title       = "Study 5",
                   subtitle    = "Lab  |  N = 206",
                   show_y      = FALSE,
                   show_legend = TRUE)

# ── Forest plot (Panel F) — same as fig_replication ───────────────────────────
forest_df <- data.frame(
  label     = c("Study 1", "Study 2", "Study 3 *",
                "Study 4", "Study 5", "Pooled"),
  r_val     = c(-0.110, -0.109, -0.184, -0.076, -0.058, -0.107),
  r_lower   = c(-0.183, -0.178, -0.202, -0.145, -0.093, -0.151),
  r_upper   = c(-0.037, -0.040, -0.166, -0.007, -0.023, -0.064),
  is_pooled = c(FALSE, FALSE, FALSE, FALSE, FALSE, TRUE),
  is_fixed  = c(FALSE, FALSE, TRUE,  FALSE, FALSE, FALSE)
)

display_order <- c("Study 1", "Study 2", "Study 3 *",
                   "Study 4", "Study 5", "Pooled")

p_forest <- ggplot(forest_df,
                   aes(x = r_val, y = label,
                       xmin = r_lower, xmax = r_upper)) +
  scale_y_discrete(limits = rev(display_order),
                   expand  = expansion(add = 0.7)) +
  geom_vline(xintercept = 0, linetype = "dashed",
             colour = "grey50", linewidth = 0.5) +
  geom_hline(yintercept = 1.5, colour = "grey40", linewidth = 0.5) +
  geom_errorbarh(data   = function(d) dplyr::filter(d, !is_pooled),
                 height = 0.2, linewidth = 0.7, colour = "black") +
  geom_point(data  = function(d) dplyr::filter(d, !is_pooled, !is_fixed),
             shape = 15, size = 3.5, colour = "black") +
  geom_point(data  = function(d) dplyr::filter(d, is_fixed),
             shape = 17, size = 3.5, colour = "black") +
  geom_errorbarh(data   = function(d) dplyr::filter(d, is_pooled),
                 height = 0.2, linewidth = 1, colour = col_missed) +
  geom_point(data  = function(d) dplyr::filter(d, is_pooled),
             shape = 18, size = 5, colour = col_missed) +
  scale_x_continuous(limits = c(-0.24, 0.04),
                     breaks = c(-0.2, -0.1, 0.0),
                     labels = c("-0.2", "-0.1", "0.0")) +
  labs(x        = expression(paste("Partial ", italic(r))),
       y        = NULL,
       title    = "H4B: Change \u00d7 Accuracy",
       subtitle = "95% CI  |  RE meta-analysis") +
  theme_minimal(base_size = 11) +
  theme(
    plot.title         = element_text(face = "bold", size = 11),
    plot.subtitle      = element_text(size = 9, colour = "grey40"),
    panel.grid.major.y = element_blank(),
    panel.grid.minor   = element_blank(),
    axis.text.y        = element_text(size = 10)
  )

# ── Combine ───────────────────────────────────────────────────────────────────
p_combined <- (p1 | p2 | p3) / (p4 | p5 | p_forest) +
  plot_layout(guides = "collect") +
  plot_annotation(
    tag_levels = "A",
    caption    = paste0(
      "* Study 3 used fixed change magnitudes (+/-.20 to +/-.65).\n",
      "Arousal z-scored within study. Shaded regions: 95% CI.\n",
      "Studies 3-5: colour = Detection (orange = Detected, blue = Missed); ",
      "linetype = Salience (solid = High, dashed = Low)."
    ),
    theme = theme(
      plot.tag        = element_text(face = "bold", size = 12),
      plot.caption    = element_text(size = 8.5, colour = "grey40",
                                     hjust = 0, margin = margin(t = 6)),
      legend.position = "bottom"
    )
  )

print(p_combined)

ggsave(file.path(FIG_DIR, "fig_arousal_salience.pdf"),
       plot = p_combined, width = 10, height = 7, device = "pdf")
ggsave(file.path(FIG_DIR, "fig_arousal_salience.png"),
       plot = p_combined, width = 10, height = 7, dpi = 300)
cat("Saved: fig_arousal_salience\n")

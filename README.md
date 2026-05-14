# What You Miss Won't Move You
## Awareness Connects Respiratory Change to Subjective Arousal

This repository contains analysis code and processed data for a five-study
empirical paper investigating whether conscious detection of breathing changes
is required for those changes to influence subjective arousal.

**Preregistration (Study 5):** https://bit.ly/436SSrv
**OSF archive (data, RDS objects, trial by trial QC files):** https://bit.ly/4txemZy

---

## Repository structure

```
/
├── analysis/               Main analysis pipeline (all studies)
│   ├── MainAnalysis.R      Entry point — source this to run everything
│   ├── utils.R             Helper functions
│   ├── models.R            Model-fitting functions (LMM, MAIA, etc.)
│   ├── meta_analysis.R     Random-effects meta-analysis functions
│   ├── analysis_arousal.R  H4A–H4C: arousal transfer tests
│   ├── analysis_maia.R     H3A–H3B: MAIA dissociation
│   ├── analysis_validation.R  H1, H2, H5: task validation
│   ├── analysis_study3_attraction_mediation.R
│   ├── tables_format.R     APA table formatter (reads results/ CSVs)
│   └── DataCleaning/       Study-level data cleaning scripts
│
├── study5_processing/      Study 5 physiological pipeline
│   ├── README.md           ← read this before running any physio scripts
│   └── *.R                 Processing scripts (require raw data from OSF)
│
├── data/                   Processed summary data (one row per participant)
│   ├── study1_summary.csv
│   ├── study2_summary.csv
│   ├── study3_summary.csv
│   ├── study4_summary.csv
│   └── study5_summary.csv
│
└── results/                Output CSVs from MainAnalysis.R
    ├── table_arousal.csv
    ├── table_maia.csv
    ├── meta_h4b_pooled.csv
    ├── meta_h3_maia_dissociation.csv
    └── ...
```

---

## Running the analysis

### Requirements

- R ≥ 4.2.0
- Key packages: `brms`, `lme4`, `lmerTest`, `broom.mixed`, `mediation`,
  `metafor`, `tidyverse`, `flextable`, `officer`

Install all dependencies:

```r
install.packages(c(
  "brms", "lme4", "lmerTest", "broom.mixed", "mediation", "metafor",
  "tidyverse", "readr", "tibble", "flextable", "officer",
  "BayesFactor", "MuMIn", "signal"
))
```

### Running from repo root

```r
source("analysis/MainAnalysis.R")
```

This runs all five studies in order and writes output CSVs to `results/`.
Total runtime is approximately 45–90 minutes depending on hardware
(Bayesian models in Studies 4 and 5 are the bottleneck).

### Generating tables

After `MainAnalysis.R` completes:

```r
source("analysis/tables_format.R")
```

Outputs `results/tables_main.docx` and `results/tables_supplement.docx`.

### Study 5 physiological pipeline

Raw physiological files are archived on OSF (not in this repo).
See `study5_processing/README.md` for the full pipeline and execution order.

---

## Data

`data/` contains one processed summary CSV per study (one row per participant).
These are the files read by `MainAnalysis.R`. Raw PsychoPy output, Qualtrics
exports, and physiological recordings are archived on OSF.

Participant IDs have been anonymized. No identifying information is present
in the summary CSVs.

---

## Deviations from preregistration

Study 5 was preregistered at https://osf.io/r6zja. Deviations are documented
in the Supplementary Materials (Supplementary S5).

---

## License

Code: MIT License  
Data: CC-BY 4.0


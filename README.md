# What You Miss Won't Move You
## Awareness Connects Respiratory Change to Subjective Arousal

This repository contains analysis code for a five-study empirical paper
investigating whether conscious detection of breathing changes is required
for those changes to influence subjective arousal.

**Preregistration (Study 5):** https://osf.io/r6zja/overview?view_only=4edce0bc913947d3a8491bfbdeb0deb3

**OSF archive (data, RDS objects, trial by trial QC files):** https://osf.io/g7rdb/overview?view_only=00d7f593dad94c3b9c4c34b994b8c162

**Task code (Studies 1–5):** https://anonymous.4open.science/r/BCAT2026-Tasks-9B85/

---

## Replication instructions

### Step 1 — Download the code and data

**1a. Download this repository**

Click the green **Code** button at the top of this GitHub page and choose
**Download ZIP**. Unzip it somewhere convenient (e.g. your Documents folder).
You should now have a folder — call it your *root folder* — that contains an
`Analysis/` subfolder.

**1b. Download the Data folder from OSF**

1. Go to: https://osf.io/g7rdb/files/osfstorage?view_only=00d7f593dad94c3b9c4c34b994b8c162
2. You will see a file browser listing the project files. Find the **`Data`**
   folder in the list.
3. Click the **three dots (⋯)** to the right of the `Data` folder and choose
   **Download as zip**.
4. Once downloaded, unzip it. You should get a folder called `Data` containing
   CSV files.
5. Move or copy the `Data` folder into your root folder (the same folder that
   contains `Analysis/`).

When set up correctly your folder should look like this:

```
BCAT2026/          ← this is your root folder (it can be named anything)
├── Analysis/
└── Data/
```

### Step 2 — Tell the script where to find your files

Open `Analysis/MainAnalysis.R` in RStudio (or any text editor). Near the top
you will find this line:

```r
BASE_DIR <- "."
```

Replace `"."` with the full path to your root folder. For example:

- **Windows:** `BASE_DIR <- "C:/Users/YourName/Documents/BCAT2026"`
- **Mac/Linux:** `BASE_DIR <- "/Users/YourName/Documents/BCAT2026"`

**How to find your path:**
- *Windows:* Open the root folder in File Explorer, click in the address bar at
  the top, and copy the path shown. Replace any backslashes (`\`) with forward
  slashes (`/`).
- *Mac:* Right-click the root folder in Finder, hold the Option key, and choose
  "Copy … as Pathname".
- *RStudio shortcut:* Open any file inside the root folder in RStudio, then run
  `dirname(dirname(rstudioapi::getActiveDocumentContext()$path))` in the Console
  to print the path automatically.

**How to confirm everything is in the right place:**
After setting `BASE_DIR`, run these two lines in the R Console and confirm both
print `TRUE`:

```r
file.exists(file.path(BASE_DIR, "Analysis", "MainAnalysis.R"))
file.exists(file.path(BASE_DIR, "Data"))
```

If either prints `FALSE`, double-check that `Analysis/` and `Data/` are both
inside the folder you used for `BASE_DIR`.

### Step 3 — Run the analysis

With `BASE_DIR` set correctly, run the full script from the R Console:

```r
source("Analysis/MainAnalysis.R")
```

Or open `Analysis/MainAnalysis.R` in RStudio and click **Source**.

`MainAnalysis.R` runs all five studies in order, writes result CSVs to
`Results/`, generates all manuscript figures to `Figures/`, and builds
the formatted table documents in `Tables/`. Total runtime is approximately
45–90 minutes depending on hardware (Bayesian models in Studies 4 and 5
are the bottleneck).

---

## Repository structure

```
/
├── Analysis/
│   ├── MainAnalysis.R          Entry point — source this to run everything
│   │                           (analyses, figures, and tables)
│   ├── utils.R                 Shared helper functions
│   ├── theme_bcat.R            ggplot theme
│   ├── meta_analysis.R         Random-effects meta-analysis across studies
│   │
│   ├── analysis_arousal.R      H4A–H4C: arousal transfer tests
│   ├── analysis_belt.R         Study 5 belt compliance and salience
│   ├── analysis_hbd.R          Heartbeat detection analyses
│   ├── analysis_individual_differences.R
│   ├── analysis_maia.R         H3A–H3B: MAIA dissociation
│   ├── analysis_miss_baseline.R
│   ├── analysis_s4_entrainment.R
│   ├── analysis_s7_maia_selfesteem.R
│   ├── analysis_study3_attraction_mediation.R
│   ├── analysis_study5_exploratory.R
│   ├── analysis_tce.R          TCE (threshold crossing events) analyses
│   ├── analysis_val_detection.R
│   ├── analysis_val_pilot_studies.R
│   ├── analysis_val_thresholds.R
│   ├── belt_salience_followup.R
│   ├── test_block_accuracy.R
│   ├── test_block_arousal.R
│   │
│   ├── fig_accuracy.R          Figure scripts (called by MainAnalysis.R)
│   ├── fig_arousal.R
│   ├── fig_regime_comparison.R
│   ├── fig_staircase.R
│   │
│   ├── Build_Main_Tables.R     Table-building scripts (called by MainAnalysis.R)
│   ├── Build_Reliability_Tables.R
│   ├── Build_Supplementary_Tables.R
│   │
│   ├── DataCleaning/           Study-level cleaning scripts
│   │   ├── run_all_cleaning.R
│   │   ├── study1_clean.R
│   │   ├── study2_clean.R
│   │   ├── study3_clean.R
│   │   ├── study4_clean.R
│   │   └── study5_clean.R
│   │
│   ├── ScaleReliability/       Scale reliability prep scripts
│   │   ├── Study1_PrepScales.R
│   │   ├── Study2_PrepScales.R
│   │   ├── Study3_PrepScales.R
│   │   ├── Study4_PrepScales.R
│   │   └── Study5_PrepScales.R
│   │
│   └── Study5/                 Study 5 physiological processing pipeline
│       ├── study5_processing_README.md   ← read before running physio scripts
│       ├── breath_pipeline.R
│       ├── analysis_study5.R
│       └── Intero2025_*.R      Individual processing steps
│
├── Data/                       Not in git — download from OSF archive
├── Results/                    Not in git — generated by MainAnalysis.R
├── Figures/                    Not in git — generated by MainAnalysis.R
└── Tables/                     Not in git — generated by MainAnalysis.R
```

---

## Requirements

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

---

## Data

Processed summary CSVs (one row per participant per study) are archived on
OSF and are read directly by `MainAnalysis.R`. Raw PsychoPy output, Qualtrics
exports, and physiological recordings are also on OSF.

Participant IDs have been anonymized. No identifying information is present
in the summary CSVs.

---

## Deviations from preregistration

Deviations from the Study 5 preregistration are documented in the
Supplementary Materials, available on the OSF archive: https://osf.io/g7rdb/overview?view_only=00d7f593dad94c3b9c4c34b994b8c162

---

## License

Code: MIT License  
Data: CC-BY 4.0

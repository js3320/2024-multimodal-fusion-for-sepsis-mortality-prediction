# CXR + Clinical Fusion

This repository presents my research combining **chest X-ray embeddings** with **clinical data** to predict ICU outcomes and analyze ventilator treatments.  
Precomputed image embeddings are merged with structured clinical variables into one dataset (early feature-level fusion), then interpretable models such as logistic regression and KNN are trained to explore clinical patterns, treatment response, and mortality risk.

---

## Start Here
Review these three first:
1. **`01_cxr_embedding_bucketing.ipynb`** — prepares CXR embeddings, performs bucketing/filtering  
2. **`02_clinical_mortality_baseline.ipynb`** — fuses embeddings with clinical data and builds a mortality prediction baseline  
3. **`03_PCA+clustering.ipynb`** — analyzes PEEP ventilation settings using logistic regression and interpretable metrics

---

## All Notebooks and Outputs

| Notebook | Purpose | Produces |
|-----------|----------|----------|
| **01_cxr_embedding_bucketing.ipynb** | Extract and bucket chest X-ray embeddings | `embeddings.csv`, `bucket_ids.csv` |
| **02_clinical_mortality_baseline.ipynb** | Merge embeddings with clinical data and train mortality baseline models | `fused_mortality.csv`, metrics table (ACC/AUC), ROC/PR plots |
| **03_peep_logistic_regression.ipynb** | Logistic regression for PEEP level response analysis | Model coefficients, odds ratios, AUC plots |
| **03a_mortality_peep_logistic_exploration.ipynb** | Exploratory variant testing for mortality & PEEP | Comparison tables of ORs, CIs, and p-values |
| **03b_peep_logistic_alt_spec.ipynb** | Alternate specification for PEEP logistic regression | Metrics and coefficient table |
| **04_univariate_peep_screen.ipynb** | Univariate screening of PEEP features | OR, CI, p-values per variable |
| **04a_univariate_alt_spec.ipynb** | Alternate univariate screening specification | OR table and summary plots |
| **05_knn_similarity_baseline.ipynb** | K-nearest neighbor baseline for similarity-based outcome prediction | Accuracy, F1-score, confusion matrix |
| **06_treatment_outcome_simulation.ipynb** | Simulated outcome analysis under altered treatment parameters | Simulated curves, sensitivity plots |
| **07_time_filtering_sensitivity.ipynb** | Effect of time-window filtering on prediction performance | Before/after counts, performance delta tables |

---

## How the Fusion Works

CXR embeddings (https://physionet.org/content/image-embeddings-mimic-cxr/1.0/) are merged with tabular clinical features (one row per ICU admission) using shared identifiers such as `study_id` or `hadm_id`.  
The merged dataset forms a multimodal table containing both **image-derived features** and **clinical variables**, which are then fed into interpretable machine-learning models (logistic regression, KNN, LightGBM).  
This approach—known as **early fusion**—enables clear interpretability while linking radiological features with patient outcomes and treatment factors.

---

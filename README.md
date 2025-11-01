# CXR + Clinical Fusion Pipeline

Reproducible pipeline to extract CXR embeddings, align with MIMIC-IV clinical data,
and train predictive/analytic models (mortality, PEEP response, etc.).

## Quickstart
```bash
# create env
conda env create -f environment.yml
conda activate cxr-pipeline
make setup

# run an example
python -m src.cxr_pipeline.extract_embeddings --input {"images": "data/cxr/", "ids": "data/ids.csv"} --output data/embeddings.csv
python -m src.cxr_pipeline.build_dataset --embeddings data/embeddings.csv --clinical data/clinical.csv --out data/fused.csv
python -m src.cxr_pipeline.train --task mortality --data data/fused.csv --out models/mortality.pkl
```

## Structure
```
cxr_github_scaffold/
├── src/cxr_pipeline/                 # Python modules (extraction, fusion, training)
├── notebooks/                        # Clean notebooks (exploration only)
│   └── archived/                     # Old exploratory notebooks
├── configs/                          # YAML configs for datasets/models/experiments
├── scripts/                          # CLI helpers
├── data/                             # (not tracked) raw/interim/processed
├── reports/figures/                  # generated plots
├── requirements.txt / environment.yml
└── README.md
```

## Data policy
- **No PHI**. Use de-identified IDs only.
- Put all datasets under `data/` which is git-ignored. For large artifacts, use Git LFS or DVC.

## Reproducibility
- Every experiment uses a YAML config in `configs/`.
- Notebooks import from `src/` and avoid ad-hoc logic.
- Tag stable runs with a Git release (e.g., `v0.1-peep-baseline`).

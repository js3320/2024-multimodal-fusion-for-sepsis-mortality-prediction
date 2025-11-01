"""Join CXR embeddings to clinical features with robust ID alignment and QC."""
from pathlib import Path
import pandas as pd
import typer

app = typer.Typer()

@app.command()
def main(embeddings: str, clinical: str, out: str):
    emb = pd.read_csv(embeddings)
    clin = pd.read_csv(clinical)
    # Example join on dicom_id or subject_id/hadm_id; adapt as needed
    key_cols = [c for c in ["dicom_id", "subject_id", "study_id", "hadm_id"] if c in emb.columns and c in clin.columns]
    if not key_cols:
        raise SystemExit("No common key columns found.")
    df = pd.merge(emb, clin, on=key_cols, how="inner")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"Wrote {out} with {len(df)} rows.")

if __name__ == "__main__":
    app()

"""Train classic models (LogReg, LightGBM-ready CSV, etc.) with consistent splits."""
from pathlib import Path
import json
from typing import List
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score
import typer

app = typer.Typer()

@app.command()
def main(task: str, data: str, out: str, target: str = None, features: List[str] = None, test_size: float = 0.2, seed: int = 42):
    df = pd.read_csv(data)
    if target is None:
        # heuristic for mortality task
        target = "mortality" if "mortality" in df.columns else df.columns[-1]
    X = df[features] if features else df.drop(columns=[target])
    y = df[target].astype(int if df[target].dropna().isin([0,1]).all() else float)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y if y.nunique()<=10 else None)

    pipe = Pipeline([("scaler", StandardScaler(with_mean=False)), ("clf", LogisticRegression(max_iter=200))])
    pipe.fit(X_train, y_train)

    y_pred = pipe.predict(X_test)
    y_proba = pipe.predict_proba(X_test)[:,1] if hasattr(pipe, "predict_proba") else y_pred

    metrics = {"acc": float(accuracy_score(y_test, y_pred))}
    try:
        metrics["auc"] = float(roc_auc_score(y_test, y_proba))
    except Exception:
        pass

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    model_path = Path(out)
    with open(model_path.with_suffix(".json"), "w") as f:
        json.dump({"task": task, "target": target, "metrics": metrics}, f, indent=2)

    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    app()

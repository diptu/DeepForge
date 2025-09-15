from __future__ import annotations


from datetime import datetime
from pathlib import Path
import joblib
import numpy as np


from app.core.config import settings
from app.models.model import build_model


def train_and_save() -> str:
    rng = np.random.default_rng(42)
    X = rng.normal(size=(512, 8))
    y = (X[:, 0] + 0.5 * X[:, 1] > 0).astype(int)

    model = build_model()
    model.fit(X, y)

    Path(settings.model_dir).mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = Path(settings.model_dir) / f"clf_{ts}.joblib"
    joblib.dump(model, path)
    return str(path)

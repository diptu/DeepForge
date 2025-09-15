from __future__ import annotations
from pathlib import Path
import joblib


from app.core.config import settings


_model_cache: dict[str, object] = {}


def get_model() -> object | None:
    if "model" in _model_cache:
        return _model_cache["model"]
    wdir = Path(settings.model_dir)
    paths = sorted(wdir.glob("*.joblib"))
    if not paths:
        return None
    model = joblib.load(paths[-1])
    _model_cache["model"] = model
    return model

from __future__ import annotations


import numpy as np


def predict_proba(model: object, features: list[float]) -> np.ndarray:
    import numpy as _np

    X = _np.array(features, dtype=float).reshape(1, -1)
    if hasattr(model, "predict_proba"):
        return model.predict_proba(X)
    if hasattr(model, "decision_function"):
        scores = model.decision_function(X)
        e = _np.exp(scores)
        return e / e.sum(axis=1, keepdims=True)
    raise ValueError("Model has no predict_proba/decision_function")

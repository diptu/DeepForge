# postprocessing.py
from __future__ import annotations


def to_label(probabilities: list[float]) -> int:
    return int(max(range(len(probabilities)), key=probabilities.__getitem__))

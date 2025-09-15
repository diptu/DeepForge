# preprocessing.py
from __future__ import annotations


from typing import Iterable


def clean_numeric(xs: Iterable[float]) -> list[float]:
    return [float(x) for x in xs]

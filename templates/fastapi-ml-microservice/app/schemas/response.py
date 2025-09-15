# response.py
from pydantic import BaseModel


class PredictOut(BaseModel):
    label: int
    proba: list[float]

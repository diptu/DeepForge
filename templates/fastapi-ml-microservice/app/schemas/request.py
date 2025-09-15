# request.py
from pydantic import BaseModel, Field


class PredictIn(BaseModel):
    features: list[float] = Field(..., min_items=1)

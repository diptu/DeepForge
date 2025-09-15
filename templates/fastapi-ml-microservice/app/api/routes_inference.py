from fastapi import APIRouter, HTTPException
from app.schemas.request import PredictIn
from app.schemas.response import PredictOut
from app.services.inference_service import predict_proba
from app.services.loader import get_model


router = APIRouter(tags=["inference"])


@router.post("/predict", response_model=PredictOut)
async def predict(req: PredictIn) -> PredictOut:
    model = get_model()
    proba = predict_proba(model, req.features)
    if proba is None:
        raise HTTPException(500, "model not loaded")
    label = int(proba.argmax())
    return PredictOut(label=label, proba=proba.tolist())

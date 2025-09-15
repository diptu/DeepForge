from fastapi import APIRouter
from app.services.training_service import train_and_save


router = APIRouter(tags=["train"])


@router.post("/train")
async def train() -> dict[str, str]:
    path = train_and_save()
    return {"ok": "true", "artifact": path}

from fastapi import FastAPI
from app.api.routes_health import router as health
from app.api.routes_inference import router as infer
from app.api.routes_train import router as train


app = FastAPI(title="ML Microservice")
app.include_router(health, prefix="/api")
app.include_router(infer, prefix="/api")
app.include_router(train, prefix="/api")


# @app.get("/health")
# async def root_health() -> dict[str, str]:
#     return {"status": "ok"}

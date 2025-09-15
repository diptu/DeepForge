from pydantic import BaseModel


class Settings(BaseModel):
    model_dir: str = "app/models/weights"
    seed: int = 42


settings = Settings()

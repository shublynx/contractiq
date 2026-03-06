from pydantic import BaseModel
import os


class Settings(BaseModel):
    service_name: str = os.getenv("SERVICE_NAME", "ContractIQ")
    environment: str = os.getenv("ENVIRONMENT", "development")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    model_mode: str = os.getenv("MODEL_MODE", "mock")


settings = Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    APP_NAME: str = "FastAPI Demo"
    LOG_LEVEL: str = "INFO"
    AUTO_CREATE_DB: bool = False
    DATABASE_URL: str = Field(...)
    REDIS_URL: str = Field(...)
    JWT_SECRET: str = Field(..., min_length=8)
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRES_MINUTES: int = 60
    FMP_API_KEY: str = ""

settings = Settings()

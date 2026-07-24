"""Application configuration."""

from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Application settings."""

    # API
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "HXAI"
    PROJECT_VERSION: str = "0.1.0"

    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:dev@localhost:5432/hxai_db",
    )
    SQLALCHEMY_ECHO: bool = True

    # JWT
    JWT_SECRET: str = os.getenv("JWT_SECRET", "your-secret-key-change-this")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24

    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    # AI Models
    MISTRAL_API_KEY: str = os.getenv("MISTRAL_API_KEY", "")
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    # Environment
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="RISK_",
        extra="ignore",
    )

    app_name: str = Field(default="financial-risk-control")
    env: str = Field(default="dev")
    log_level: str = Field(default="INFO")
    timezone: str = Field(default="UTC")
    risk_threshold: float = Field(default=0.8, ge=0.0, le=1.0)
    api_token: str = Field(default="dev-token")


@lru_cache(maxsize=1)
def get_settings() -> AppSettings:
    return AppSettings()

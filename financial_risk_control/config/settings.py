from pydantic import BaseModel, Field


class AppSettings(BaseModel):
    app_name: str = Field(default="financial-risk-control")
    env: str = Field(default="dev")
    log_level: str = Field(default="INFO")
    timezone: str = Field(default="UTC")


SETTINGS = AppSettings()

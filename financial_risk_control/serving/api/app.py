from fastapi import FastAPI

from financial_risk_control.config.settings import get_settings
from financial_risk_control.serving.api.middleware.auth import auth_middleware
from financial_risk_control.serving.api.middleware.logging import logging_middleware
from financial_risk_control.serving.api.routers.monitor_api import router as monitor_router
from financial_risk_control.serving.api.routers.risk_api import router as risk_router

settings = get_settings()
app = FastAPI(title=settings.app_name)
app.middleware("http")(logging_middleware)
app.middleware("http")(auth_middleware)
app.include_router(risk_router, prefix="/api/v1")
app.include_router(monitor_router, prefix="/api/v1")

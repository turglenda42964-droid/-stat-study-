from fastapi import FastAPI

from financial_risk_control.serving.api.routers.monitor_api import router as monitor_router
from financial_risk_control.serving.api.routers.risk_api import router as risk_router

app = FastAPI(title="Financial Risk Control")
app.include_router(risk_router, prefix="/api/v1")
app.include_router(monitor_router, prefix="/api/v1")

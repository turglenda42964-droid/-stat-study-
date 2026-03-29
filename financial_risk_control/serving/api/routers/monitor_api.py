from fastapi import APIRouter

from financial_risk_control.config.settings import get_settings

router = APIRouter(tags=["monitor"])


@router.get("/monitor/health")
def health() -> dict:
    settings = get_settings()
    return {"status": "ok", "app": settings.app_name, "env": settings.env}

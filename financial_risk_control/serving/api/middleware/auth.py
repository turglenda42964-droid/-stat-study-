from fastapi import Request
from starlette.responses import JSONResponse

from financial_risk_control.config.settings import get_settings


async def auth_middleware(request: Request, call_next):
    if request.url.path.startswith("/api/v1/risk"):
        token = request.headers.get("X-API-Token")
        if token != get_settings().api_token:
            return JSONResponse(status_code=401, content={"detail": "unauthorized"})

    return await call_next(request)

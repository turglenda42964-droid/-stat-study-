import logging
import time

from fastapi import Request

logger = logging.getLogger("risk.api")


async def logging_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    cost = time.perf_counter() - start
    response.headers["X-Process-Time"] = f"{cost:.6f}"
    logger.info("path=%s status=%s cost=%.6f", request.url.path, response.status_code, cost)
    return response

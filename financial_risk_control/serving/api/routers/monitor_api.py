from fastapi import APIRouter

router = APIRouter(tags=["monitor"])


@router.get("/monitor/health")
def health() -> dict:
    return {"status": "ok"}

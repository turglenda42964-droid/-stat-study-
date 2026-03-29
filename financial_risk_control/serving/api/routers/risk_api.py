from fastapi import APIRouter

router = APIRouter(tags=["risk"])


@router.post("/risk/score")
def score(payload: dict) -> dict:
    return {"risk_score": 0.42, "input": payload}

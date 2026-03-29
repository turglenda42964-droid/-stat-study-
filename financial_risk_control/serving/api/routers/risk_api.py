from pydantic import BaseModel, Field
from fastapi import APIRouter

from financial_risk_control.serving.realtime.decision_service import RealtimeDecisionService

router = APIRouter(tags=["risk"])
_service = RealtimeDecisionService()


class RiskScoreRequest(BaseModel):
    customer_id: str
    amount: float = Field(ge=0)
    night_ratio: float = Field(default=0.0, ge=0.0, le=1.0)


class RiskScoreResponse(BaseModel):
    risk_score: float
    action: str
    reasons: list[str]


@router.post("/risk/score", response_model=RiskScoreResponse)
def score(payload: RiskScoreRequest) -> RiskScoreResponse:
    result = _service.decide(payload.model_dump())
    return RiskScoreResponse(
        risk_score=result["context"]["score"],
        action=result["action"],
        reasons=result.get("reasons", []),
    )

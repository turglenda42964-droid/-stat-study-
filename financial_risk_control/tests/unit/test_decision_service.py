from financial_risk_control.serving.realtime.decision_service import RealtimeDecisionService


def test_decision_service_output_contains_action_and_score() -> None:
    svc = RealtimeDecisionService()
    result = svc.decide({"amount": 12000, "night_ratio": 0.5})
    assert result["action"] in {"PASS", "REVIEW", "BLOCK"}
    assert 0.0 <= result["context"]["score"] <= 1.0

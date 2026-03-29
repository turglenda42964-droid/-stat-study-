from financial_risk_control.decision_engine.policies.policy_manager import Policy
from financial_risk_control.decision_engine.workflows.risk_workflow import RiskWorkflow


class RealtimeDecisionService:
    def __init__(self) -> None:
        self.workflow = RiskWorkflow()
        self.default_policy = Policy(
            name="default_retail_policy",
            version=1,
            block_when_high_risk=True,
            review_band=(0.5, 0.8),
        )

    def score(self, event: dict) -> float:
        amount = float(event.get("amount", 0.0))
        night_ratio = float(event.get("night_ratio", 0.0))
        score = min(1.0, 0.00001 * amount + 0.4 * night_ratio)
        return round(score, 4)

    def decide(self, event: dict) -> dict:
        context = {**event, "score": self.score(event)}
        return self.workflow.run(policy=self.default_policy, context=context)

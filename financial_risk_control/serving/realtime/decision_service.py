from financial_risk_control.decision_engine.workflows.risk_workflow import RiskWorkflow


class RealtimeDecisionService:
    def __init__(self) -> None:
        self.workflow = RiskWorkflow()

    def decide(self, event: dict) -> dict:
        policy = {"block_when_high_risk": True}
        return self.workflow.run(policy=policy, context=event)

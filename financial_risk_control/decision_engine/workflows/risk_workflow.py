from financial_risk_control.decision_engine.policies.policy_executor import PolicyExecutor


class RiskWorkflow:
    def __init__(self) -> None:
        self.executor = PolicyExecutor()

    def run(self, policy: dict, context: dict) -> dict:
        action = self.executor.execute(policy, context)
        return {"action": action, "context": context}

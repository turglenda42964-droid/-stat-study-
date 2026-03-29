from financial_risk_control.decision_engine.policies.policy_executor import PolicyExecutor
from financial_risk_control.decision_engine.policies.policy_manager import Policy
from financial_risk_control.decision_engine.rules.basic_rules import amount_under_limit
from financial_risk_control.decision_engine.rules.rule_engine import RuleEngine


class RiskWorkflow:
    def __init__(self) -> None:
        self.executor = PolicyExecutor()
        self.rule_engine = RuleEngine()
        self.rule_engine.register("amount_under_limit", amount_under_limit)

    def run(self, policy: Policy, context: dict) -> dict:
        rule_result = self.rule_engine.evaluate(context)
        if not rule_result.passed:
            return {"action": "BLOCK", "reasons": rule_result.failed_rules, "context": context}

        decision = self.executor.execute(policy, context)
        return {"action": decision.action, "reasons": decision.reasons, "context": context}

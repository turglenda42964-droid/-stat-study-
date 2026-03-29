from dataclasses import dataclass

from financial_risk_control.decision_engine.policies.policy_manager import Policy


@dataclass
class Decision:
    action: str
    reasons: list[str]


class PolicyExecutor:
    def execute(self, policy: Policy, context: dict) -> Decision:
        score = float(context.get("score", 0.0))
        if policy.block_when_high_risk and score >= 0.8:
            return Decision(action="BLOCK", reasons=["risk_score_above_threshold"])

        lower, upper = policy.review_band
        if lower <= score < upper:
            return Decision(action="REVIEW", reasons=["risk_score_in_review_band"])

        return Decision(action="PASS", reasons=["risk_score_low"])

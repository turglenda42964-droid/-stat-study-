from financial_risk_control.decision_engine.policies.policy_executor import PolicyExecutor
from financial_risk_control.decision_engine.policies.policy_manager import Policy


def test_policy_executor_blocks_high_risk() -> None:
    executor = PolicyExecutor()
    policy = Policy(name="p1", version=1, block_when_high_risk=True)
    result = executor.execute(policy, {"score": 0.95})
    assert result.action == "BLOCK"


def test_policy_executor_reviews_medium_risk() -> None:
    executor = PolicyExecutor()
    policy = Policy(name="p1", version=1, block_when_high_risk=True, review_band=(0.5, 0.8))
    result = executor.execute(policy, {"score": 0.55})
    assert result.action == "REVIEW"

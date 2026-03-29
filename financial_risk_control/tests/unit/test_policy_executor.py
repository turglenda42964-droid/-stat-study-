from financial_risk_control.decision_engine.policies.policy_executor import PolicyExecutor


def test_policy_executor_blocks_high_risk() -> None:
    executor = PolicyExecutor()
    result = executor.execute({"block_when_high_risk": True}, {"score": 0.95})
    assert result == "BLOCK"

class PolicyExecutor:
    def execute(self, policy: dict, context: dict) -> str:
        if policy.get("block_when_high_risk") and context.get("score", 0) > 0.8:
            return "BLOCK"
        return "PASS"

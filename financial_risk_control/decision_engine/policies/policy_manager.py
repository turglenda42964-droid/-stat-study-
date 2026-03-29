from dataclasses import dataclass


@dataclass
class Policy:
    name: str
    version: int
    block_when_high_risk: bool
    review_band: tuple[float, float] = (0.5, 0.8)


class PolicyManager:
    def __init__(self) -> None:
        self._policies: dict[str, Policy] = {}

    def upsert(self, policy: Policy) -> None:
        current = self._policies.get(policy.name)
        if current and policy.version < current.version:
            raise ValueError("policy version regression")
        self._policies[policy.name] = policy

    def get(self, name: str) -> Policy:
        return self._policies[name]

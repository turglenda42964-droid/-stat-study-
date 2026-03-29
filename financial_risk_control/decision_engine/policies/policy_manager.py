class PolicyManager:
    def __init__(self) -> None:
        self._policies: dict[str, dict] = {}

    def upsert(self, name: str, policy: dict) -> None:
        self._policies[name] = policy

    def get(self, name: str) -> dict:
        return self._policies[name]

from collections.abc import Callable


class RuleEngine:
    def __init__(self) -> None:
        self.rules: list[Callable[[dict], bool]] = []

    def register(self, rule: Callable[[dict], bool]) -> None:
        self.rules.append(rule)

    def evaluate(self, context: dict) -> bool:
        return all(rule(context) for rule in self.rules)

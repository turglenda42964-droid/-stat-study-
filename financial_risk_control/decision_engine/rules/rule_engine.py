from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class RuleResult:
    passed: bool
    failed_rules: list[str]


class RuleEngine:
    def __init__(self) -> None:
        self.rules: list[tuple[str, Callable[[dict], bool]]] = []

    def register(self, name: str, rule: Callable[[dict], bool]) -> None:
        self.rules.append((name, rule))

    def evaluate(self, context: dict) -> RuleResult:
        failed = [name for name, fn in self.rules if not fn(context)]
        return RuleResult(passed=not failed, failed_rules=failed)

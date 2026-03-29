from dataclasses import dataclass
from typing import Any


@dataclass
class ValidationResult:
    ok: bool
    errors: list[str]


def validate_required_fields(payload: dict[str, Any], required: list[str]) -> ValidationResult:
    missing = [f for f in required if payload.get(f) in (None, "")]
    return ValidationResult(ok=not missing, errors=[f"missing_required:{f}" for f in missing])


def validate_amount(amount: float) -> ValidationResult:
    if amount < 0:
        return ValidationResult(ok=False, errors=["amount_must_be_non_negative"])
    return ValidationResult(ok=True, errors=[])

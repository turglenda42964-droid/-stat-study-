from dataclasses import dataclass


@dataclass
class ValidationResult:
    ok: bool
    errors: list[str]


def validate_required_fields(payload: dict, required: list[str]) -> ValidationResult:
    missing = [f for f in required if f not in payload]
    return ValidationResult(ok=not missing, errors=missing)

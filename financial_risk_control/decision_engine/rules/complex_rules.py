def low_risk_segment(context: dict) -> bool:
    score = float(context.get("score", 1))
    return score < 0.3 and context.get("segment") in {"A", "B"}

def drift_score(reference: list[float], current: list[float]) -> float:
    if not reference or not current:
        return 0.0
    return abs(sum(reference) / len(reference) - sum(current) / len(current))

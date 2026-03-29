def amount_under_limit(context: dict, limit: float = 50000.0) -> bool:
    return float(context.get("amount", 0)) <= limit

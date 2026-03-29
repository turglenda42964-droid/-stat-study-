from functools import lru_cache


@lru_cache(maxsize=256)
def cached_score_bucket(score: float) -> str:
    if score >= 0.8:
        return "high"
    if score >= 0.4:
        return "medium"
    return "low"

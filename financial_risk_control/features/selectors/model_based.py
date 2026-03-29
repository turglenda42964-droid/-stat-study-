from typing import Sequence


def top_k_by_importance(feature_names: Sequence[str], importances: Sequence[float], k: int) -> list[str]:
    ranked = sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)
    return [name for name, _ in ranked[:k]]

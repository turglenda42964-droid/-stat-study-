class WeightedEnsemble:
    def __init__(self, weights: dict[str, float]):
        self.weights = weights

    def blend(self, predictions: dict[str, list[float]]) -> list[float]:
        if not predictions:
            return []
        names = list(predictions.keys())
        length = len(predictions[names[0]])
        out = [0.0] * length
        for name, vals in predictions.items():
            w = self.weights.get(name, 0.0)
            for i, v in enumerate(vals):
                out[i] += w * v
        return out

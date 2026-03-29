from .base import RiskBaseModel


class FeatureVector(RiskBaseModel):
    customer_id: str
    values: dict[str, float]

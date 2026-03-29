from financial_risk_control.models.base_model import BaseRiskModel


class LightGBMRiskModel(BaseRiskModel):
    def fit(self, X, y) -> None:
        _ = (X, y)

    def predict_proba(self, X):
        _ = X
        return []

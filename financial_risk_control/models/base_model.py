from abc import ABC, abstractmethod


class BaseRiskModel(ABC):
    @abstractmethod
    def fit(self, X, y) -> None:
        raise NotImplementedError

    @abstractmethod
    def predict_proba(self, X):
        raise NotImplementedError

from datetime import datetime

from .base import RiskBaseModel


class RawRiskEvent(RiskBaseModel):
    event_id: str
    customer_id: str
    amount: float
    event_time: datetime

from pydantic import BaseModel


class RiskBaseModel(BaseModel):
    model_config = {"from_attributes": True}

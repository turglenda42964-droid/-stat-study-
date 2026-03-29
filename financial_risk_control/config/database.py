from pydantic import BaseModel, Field


class DatabaseConfig(BaseModel):
    dsn: str = Field(default="postgresql://risk:risk@localhost:5432/riskdb")
    pool_size: int = Field(default=10, ge=1)
    max_overflow: int = Field(default=20, ge=0)


DATABASE_CONFIG = DatabaseConfig()

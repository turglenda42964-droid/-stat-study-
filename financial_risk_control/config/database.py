from pydantic import BaseModel, Field


class DatabaseConfig(BaseModel):
    """Database configuration for OLTP risk event storage."""

    host: str = Field(default="localhost")
    port: int = Field(default=5432, ge=1, le=65535)
    user: str = Field(default="risk")
    password: str = Field(default="risk")
    db_name: str = Field(default="riskdb")
    pool_size: int = Field(default=10, ge=1)
    max_overflow: int = Field(default=20, ge=0)

    @property
    def dsn(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


DATABASE_CONFIG = DatabaseConfig()

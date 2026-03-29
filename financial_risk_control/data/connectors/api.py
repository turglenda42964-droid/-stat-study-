from typing import Any


class APIConnector:
    def __init__(self, base_url: str, timeout: int = 30) -> None:
        self.base_url = base_url
        self.timeout = timeout

    def get_json(self, endpoint: str) -> dict[str, Any]:
        _ = endpoint
        return {"status": "stub"}

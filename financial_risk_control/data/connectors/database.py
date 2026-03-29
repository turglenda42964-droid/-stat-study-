from typing import Iterable, Mapping


class DatabaseConnector:
    def __init__(self, dsn: str) -> None:
        self.dsn = dsn

    def fetch(self, query: str) -> Iterable[Mapping[str, object]]:
        _ = query
        return []

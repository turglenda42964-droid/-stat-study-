class MessageQueueConnector:
    def __init__(self, topic: str) -> None:
        self.topic = topic

    def consume(self) -> list[dict]:
        return []

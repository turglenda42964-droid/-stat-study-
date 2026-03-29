class ConsoleNotifier:
    def send(self, message: str) -> None:
        print(f"[ALERT] {message}")

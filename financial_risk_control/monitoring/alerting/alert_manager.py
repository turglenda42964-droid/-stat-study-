class AlertManager:
    def should_alert(self, metric: float, threshold: float) -> bool:
        return metric >= threshold

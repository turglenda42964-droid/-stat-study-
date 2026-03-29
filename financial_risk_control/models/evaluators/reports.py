def build_evaluation_report(metrics: dict[str, float]) -> str:
    lines = ["# Model Evaluation Report"]
    lines.extend(f"- {k}: {v:.4f}" for k, v in metrics.items())
    return "\n".join(lines)

import pandas as pd


def variance_threshold(df: pd.DataFrame, threshold: float = 1e-6) -> list[str]:
    variances = df.var(numeric_only=True)
    return variances[variances > threshold].index.tolist()

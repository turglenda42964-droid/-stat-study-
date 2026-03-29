import pandas as pd


def drop_high_missing(df: pd.DataFrame, threshold: float = 0.95) -> pd.DataFrame:
    max_missing = int(len(df) * threshold)
    return df.dropna(axis=1, thresh=len(df) - max_missing)

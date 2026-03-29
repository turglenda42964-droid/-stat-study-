import pandas as pd


def clip_outliers(df: pd.DataFrame, lower: float = 0.01, upper: float = 0.99) -> pd.DataFrame:
    out = df.copy()
    for col in out.select_dtypes(include=["number"]).columns:
        ql, qu = out[col].quantile([lower, upper])
        out[col] = out[col].clip(ql, qu)
    return out

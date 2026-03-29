import pandas as pd


def calc_amount_stats(df: pd.DataFrame) -> pd.DataFrame:
    g = df.groupby("customer_id")["amount"]
    return g.agg(["count", "mean", "std"]).fillna(0).reset_index()

import pandas as pd


def calc_velocity(df: pd.DataFrame, window: str = "1D") -> pd.DataFrame:
    out = df.sort_values("event_time").set_index("event_time")
    rolling = out.groupby("customer_id")["amount"].rolling(window).count()
    return rolling.reset_index(name="txn_velocity")

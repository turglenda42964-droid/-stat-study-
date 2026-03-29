import pandas as pd


def calc_behavior_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["is_night"] = out["event_time"].dt.hour.between(0, 5).astype(int)
    return out.groupby("customer_id")["is_night"].mean().reset_index(name="night_ratio")

import pandas as pd

from financial_risk_control.features.calculators.basic_features import calc_amount_stats
from financial_risk_control.features.calculators.behavior_features import calc_behavior_features


def build_feature_table(df: pd.DataFrame) -> pd.DataFrame:
    base = calc_amount_stats(df)
    behavior = calc_behavior_features(df)
    return base.merge(behavior, on="customer_id", how="left").fillna(0)

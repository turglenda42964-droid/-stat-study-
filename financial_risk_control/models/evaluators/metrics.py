from sklearn.metrics import roc_auc_score


def auc(y_true, y_score) -> float:
    return float(roc_auc_score(y_true, y_score))

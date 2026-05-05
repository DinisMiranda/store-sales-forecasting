import numpy as np


def rmsle(y_true, y_pred):
    """
    Root Mean Squared Logarithmic Error.
    Kaggle's evaluation metric for this competition.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    # Clip predictions to avoid log of negative
    y_pred = np.clip(y_pred, 0, None)
    return np.sqrt(np.mean((np.log1p(y_pred) - np.log1p(y_true)) ** 2))

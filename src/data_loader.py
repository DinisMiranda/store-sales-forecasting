import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")


def load_train():
    return pd.read_csv(DATA_DIR / "train.csv", parse_dates=["date"])


def load_test():
    return pd.read_csv(DATA_DIR / "test.csv", parse_dates=["date"])


def load_stores():
    return pd.read_csv(DATA_DIR / "stores.csv")


def load_oil():
    return pd.read_csv(DATA_DIR / "oil.csv", parse_dates=["date"])


def load_holidays():
    return pd.read_csv(DATA_DIR / "holidays_events.csv", parse_dates=["date"])


def load_transactions():
    return pd.read_csv(DATA_DIR / "transactions.csv", parse_dates=["date"])


def load_all():
    """Load and return all datasets as a dictionary."""
    return {
        "train": load_train(),
        "test": load_test(),
        "stores": load_stores(),
        "oil": load_oil(),
        "holidays": load_holidays(),
        "transactions": load_transactions(),
    }

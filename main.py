import pandas as pd

from utils import normalize

if __name__ == "__main__":
    df = normalize(pd.read_csv("balance.csv"))
    df.to_csv("balance-transformed.csv")

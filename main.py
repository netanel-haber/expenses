import pandas as pd
import column as cl
import numpy as np
from normalize import normalize
import matplotlib.pyplot as plt


def create_pivot_table(path) -> pd.DataFrame:
    df = normalize(pd.read_csv(path, thousands=","))
    return df.pivot_table(
        index=[df[cl.DATE].dt.year, df[cl.DATE].dt.month],
        columns=cl.ACTION,
        values=cl.DIFF,
        aggfunc=np.sum,
    )


if __name__ == "__main__":
    create_pivot_table("balance.csv").plot.bar(stacked=True)
    plt.show()

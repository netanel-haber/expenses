import pandas as pd
import column as cl
import category as ca
from normalize import normalize
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df = normalize(pd.read_csv("balance.csv", thousands=","))

    df.pivot_table(
        index=[df[cl.DATE].dt.year, df[cl.DATE].dt.month],
        columns=cl.ACTION,
        values=cl.DIFF,
    ).plot.bar(stacked=True)

    plt.show()

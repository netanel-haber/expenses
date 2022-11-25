import pandas as pd
import column as cl
import category as ca
from utils import normalize
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df = normalize(pd.read_csv("balance.csv", thousands=",")).reindex(
        columns=[cl.ACTION, cl.DATE, cl.DIFF]
    )

    # by_date_and_action = (

    #     .groupby([df[cl.DATE].dt.year, df[cl.DATE].dt.month])
    #     .sum(numeric_only=True)
    # )

    df.pivot_table(
        index=[df[cl.DATE].dt.year, df[cl.DATE].dt.month],
        columns=cl.ACTION,
        values=cl.DIFF,
    ).plot(kind="bar", stacked=True)

    plt.show(block=False)

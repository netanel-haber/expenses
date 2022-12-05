import pandas as pd
import column as cl
import numpy as np
from normalize import normalize
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def render_pivot_table(path) -> Figure:
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)

    df = normalize(pd.read_csv(path, thousands=","))
    table = df.pivot_table(
        index=[df[cl.DATE].dt.year, df[cl.DATE].dt.month],
        columns=cl.ACTION,
        values=cl.DIFF,
        aggfunc=np.sum,
    )
    table.plot.bar(stacked=True, ax=ax)

    return fig


if __name__ == "__main__":
    render_pivot_table("balance.csv")

from __future__ import annotations
import pandas as pd
import seaborn as sns
import matplotlib as mpl
from matplotlib import pyplot as plt
from typing import TYPE_CHECKING

mpl.use("Agg")

if TYPE_CHECKING:
    from matplotlib.figure import Figure
    from matplotlib.axis import Axis


def _reformat_axis_label(axis: Axis) -> None:
    axis.set_label_text(
        " ".join(s.capitalize() for s in axis.get_label_text().split("_"))
    )


def create_optical_density_boxplot(
    dataframe: pd.DataFrame,
    column: str = "optical_density",
    aa_sequence_name: str = "amino_acid_sequence",
) -> Figure:
    fig, axes = plt.subplots(1, dpi=300, figsize=(10, 8))
    sns.boxplot(
        data=dataframe,
        x=column,
        y=aa_sequence_name,
        ax=axes,
        fill=False,
        dodge=True,
        gap=0.2,
        medianprops={"color": "r", "linewidth": 2},
    )
    axes.grid(axis="x", which="both")
    axes.grid(axis="y")
    axes.tick_params(axis="y", which="major", labelsize=10)
    _reformat_axis_label(axes.get_xaxis())
    _reformat_axis_label(axes.get_yaxis())
    fig.suptitle("Optical Density Range of Amino Acid Sequences")
    fig.tight_layout()
    return fig


def create_histograms(
    dataframe: pd.DataFrame,
    column: str = "optical_density",
    aa_sequence_name: str = "amino_acid_sequence",
) -> Figure:
    with sns.axes_style("whitegrid"):
        g = sns.catplot(
            data=dataframe,
            y=column,
            col=aa_sequence_name,
            kind="count",
            height=4,
            aspect=0.6,
            col_wrap=13,
            sharex=True,
            orient="v",
        )
        g.set_ylabels(" ".join(s.capitalize() for s in column.split("_")))
        g.set_xlabels("Count")
        g.set_titles("{col_name}")
        fig = g.figure

    fig.suptitle("Optical Density Counts for Amino Acid Sequences")
    fig.tight_layout()
    return fig

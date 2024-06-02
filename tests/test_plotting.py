from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from typing import TYPE_CHECKING

from atat import plotting

if TYPE_CHECKING:
    from pandas import DataFrame


def test_creates_plot(input_dataframe: DataFrame) -> None:
    figure: Figure = plotting.plot_optical_densities(input_dataframe)

    assert isinstance(figure, Figure), "returned value is not a matplotlib Figure"

    axes = figure.get_axes()
    assert axes, "returned Figure as no axes"

    for i, axis in enumerate(axes):
        assert axis.has_data(), f"Axis {i} has no data set"

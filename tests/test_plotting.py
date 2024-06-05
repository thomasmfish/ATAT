from __future__ import annotations
import pytest

from matplotlib.figure import Figure
from typing import TYPE_CHECKING

from atat import plotting

if TYPE_CHECKING:
    from pandas import DataFrame


@pytest.mark.skip(
    "Plotting is not 100%% consistent on different systems, so manual checking is required"
)
def test_create_optical_density_boxplot(input_dataframe: DataFrame) -> None:
    figure = plotting.create_optical_density_boxplot(input_dataframe)

    assert isinstance(figure, Figure), "returned value is not a matplotlib Figure"

    figure.show()

    axes = figure.get_axes()
    assert axes, "returned Figure as no axes"

    for i, axis in enumerate(axes):
        assert axis.has_data(), f"Axis {i} has no data set"


@pytest.mark.skip(
    "Plotting is not 100%% consistent on different systems, so manual checking is required"
)
def test_create_histograms(input_dataframe: DataFrame) -> None:
    figure = plotting.create_histograms(input_dataframe)

    assert isinstance(figure, Figure), "returned value is not a matplotlib Figure"

    figure.show()

    axes = figure.get_axes()
    assert axes, "returned Figure as no axes"

    for i, axis in enumerate(axes):
        assert axis.has_data(), f"Axis {i} has no data set"

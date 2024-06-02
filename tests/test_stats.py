from __future__ import annotations

import pytest
from pandas.testing import assert_frame_equal
from typing import TYPE_CHECKING

from atat import stats
from atat.exceptions import DuplicateIndexError

from .utils import create_dataframe_with_duplicate


if TYPE_CHECKING:
    import pandas as pd


def test_analyse_statistics(
    input_dataframe: pd.DataFrame, output_dataframe: pd.DataFrame
) -> None:
    assert_frame_equal(stats.analyse_statistics(input_dataframe), output_dataframe)


@pytest.mark.parametrize(
    "dataframe_with_duplicate,dataframe_without_duplicate,expected_exception",
    [
        (*create_dataframe_with_duplicate(False, False), DuplicateIndexError),
        (*create_dataframe_with_duplicate(True, False), DuplicateIndexError),
        (*create_dataframe_with_duplicate(False, True), DuplicateIndexError),
        (*create_dataframe_with_duplicate(True, True), None),
    ],
    ids=[
        "only index matches",
        "different optical density",
        "different sequence",
        "full duplicate",
    ],
)
def test_remove_duplicate_entries(
    dataframe_with_duplicate: pd.DataFrame,
    dataframe_without_duplicate: pd.DataFrame,
    expected_exception: Exception | None,
) -> None:
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            stats.remove_duplicates(dataframe_with_duplicate)
    else:
        assert_frame_equal(
            stats.remove_duplicates(dataframe_with_duplicate),
            dataframe_without_duplicate,
        )


def test_group_values_per_dataset(input_dataframe: pd.DataFrame) -> None: ...


def test_get_min_optical_densities(
    input_dataframe: pd.DataFrame, output_dataframe: pd.DataFrame
):
    stats.get_minimum_optical_densities(input_dataframe)


def test_get_max_optical_densities(
    input_dataframe: pd.DataFrame, output_dataframe: pd.DataFrame
): ...


def test_get_mean_optical_densities(
    input_dataframe: pd.DataFrame, output_dataframe: pd.DataFrame
): ...

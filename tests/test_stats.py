from __future__ import annotations

import pytest
from pandas.testing import assert_frame_equal, assert_series_equal
from numpy.testing import assert_array_equal, assert_almost_equal

import pandas as pd
import numpy as np
from collections import namedtuple
from typing import TYPE_CHECKING

from atat import stats
from atat.exceptions import DuplicateIndexError

from .utils import create_dataframe_with_duplicate


if TYPE_CHECKING:
    from collections.abc import Collection
    import pandas as pd
    from numpy.typing import NDArray

GroupedFrameTestData = namedtuple("GroupedFrameTestData", ["dataframe", "dict"])


@pytest.fixture
def grouped_frame_test_data() -> dict[str, NDArray[np.float64]]:
    aa_sequences = ["GFTFSSYF", "GFTFSNYA", "GFTFSSYW", "GFPFEMYD", "GFTFDDYA"]

    grouped_densities = {}

    for i, aa_sequence in enumerate(aa_sequences):
        # Setting size by i ensures a range of quantities to group
        grouped_densities[aa_sequence] = np.random.rand(i + 1)

    return grouped_densities


def grouped_frame_test_data_to_dataframe(
    grouped_frame_test_data: dict[str, NDArray[np.float64]], columns: Collection[str]
) -> pd.DataFrame:
    # Organise into file-like structure, with randomised order
    data = []
    for aa_sequence, densities in grouped_frame_test_data.items():
        data.extend((density, aa_sequence) for density in densities)
    np.random.shuffle(data)
    return pd.DataFrame(data, columns=columns)


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


def test_group_dataframe_by_amino_acid_sequence(grouped_frame_test_data) -> None:
    columns = ["optical_density", "amino_acid_sequence"]

    # Create input dataframe
    input_dataframe = grouped_frame_test_data_to_dataframe(
        grouped_frame_test_data, columns
    )

    grouped_dataframe = stats.group_dataframe_by_amino_acid_sequence(input_dataframe)

    for name, group in grouped_dataframe:
        # Cannot check DataFrameGroupBy data directly
        # checking stats is the a decent proxy
        # Checking all of these is probably overkill
        name = name[0]
        assert_array_equal(
            group.count().get(columns[0]),
            len(grouped_frame_test_data[name]),
            err_msg=f"{name} doesn't match",
        )
        assert_almost_equal(
            group.sum(numeric_only=True).get(columns[0]),
            grouped_frame_test_data[name].sum(),
            err_msg=f"{name} doesn't match",
        )
        assert_almost_equal(
            group.mean(numeric_only=True).get(columns[0]),
            grouped_frame_test_data[name].mean(),
            err_msg=f"{name} doesn't match",
        )
        assert_almost_equal(
            group.median(numeric_only=True).get(columns[0]),
            np.median(grouped_frame_test_data[name]),
            err_msg=f"{name} doesn't match",
        )


@pytest.mark.parametrize(
    "statistics", [("mean", "max", "min"), ("min", "max"), ("mean",)]
)
def test_get_statistics_from_grouped_dataframe(
    statistics: tuple[str, ...], grouped_frame_test_data
) -> None:
    stat_name_to_numpy_function = {"mean": np.mean, "max": np.max, "min": np.min}

    columns = ["optical_density", "amino_acid_sequence"]
    expected_columns = [
        "amino_acid_sequence",
        *(f"{stat}_{columns[0]}" for stat in statistics),
    ]

    # Create input dataframe
    input_grouped_dataframe = stats.group_dataframe_by_amino_acid_sequence(
        grouped_frame_test_data_to_dataframe(grouped_frame_test_data, columns)
    )

    stats_dataframe = stats.get_statistics_from_grouped_dataframe(
        input_grouped_dataframe, statistics
    )

    series_list = []
    for aa_sequence, densities in grouped_frame_test_data.items():
        series_list.append(
            pd.Series(
                [
                    aa_sequence,
                    *(
                        stat_name_to_numpy_function[stat](densities)
                        for stat in statistics
                    ),
                ],
                index=expected_columns,
            )
        )
    for (_, series), expected_series in zip(stats_dataframe.iterrows(), series_list):
        assert_series_equal(series, expected_series)

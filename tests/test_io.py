from __future__ import annotations

from pandas.testing import assert_frame_equal
import filecmp

from typing import TYPE_CHECKING

from atat import file_handling

if TYPE_CHECKING:
    from pathlib import Path
    from pandas import DataFrame


def test_reads_input(input_data_path: Path, input_dataframe: DataFrame) -> None:
    assert_frame_equal(file_handling.read_input(input_data_path), input_dataframe)


def test_saves_output(
    output_dataframe: DataFrame, output_data_path: Path, tmp_path
) -> None:
    tmp_output_path = tmp_path / "output_data.csv"
    file_handling.save_data(tmp_output_path, output_dataframe)
    assert filecmp.cmp(
        tmp_output_path, output_data_path, shallow=False
    ), "Output files do not match"

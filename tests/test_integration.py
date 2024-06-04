from __future__ import annotations
import filecmp
from typing import TYPE_CHECKING

import atat

if TYPE_CHECKING:
    import pandas as pd
    from pathlib import Path


def test_create_statistical_output(
    input_dataframe: pd.DataFrame, output_data_path: Path, tmp_path
) -> None:
    tmp_output = tmp_path / "output_data.csv"
    atat.create_statistical_output(tmp_output, input_dataframe)

    assert tmp_output.is_file()

    assert filecmp.cmp(tmp_output, output_data_path)


def test_create_optical_density_plot(
    input_dataframe: pd.DataFrame, output_plot_path: Path, tmp_path
) -> None:
    tmp_output = tmp_path / "output_plot.png"

    atat.create_optical_density_plot(tmp_output, input_dataframe)

    assert tmp_output.is_file()

    assert filecmp.cmp(tmp_output, output_plot_path, shallow=False)


def test_run(input_dataframe, output_data_path, output_plot_path, tmp_path) -> None:
    output_name = "output"
    tmp_output_data_path = tmp_path / f"{output_name}.csv"
    tmp_output_plot_path = tmp_path / f"{output_name}.png"

    atat.run(
        input_dataframe,
        tmp_path,
        output_name,
    )

    assert tmp_output_data_path.is_file()

    assert tmp_output_plot_path.is_file()

    assert filecmp.cmp(
        tmp_output_data_path, output_data_path, shallow=False
    ), "Output files do not match"

    assert filecmp.cmp(
        tmp_output_plot_path, output_plot_path, shallow=False
    ), "Output files do not match"

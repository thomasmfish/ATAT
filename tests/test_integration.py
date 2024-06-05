from __future__ import annotations
import filecmp
from typing import TYPE_CHECKING

from atat.main import run

if TYPE_CHECKING:
    import pandas as pd
    from pathlib import Path


def test_create_statistical_output(
    input_data_path: pd.DataFrame, output_data_path: Path, tmp_path
) -> None:
    output_name = "output"
    tmp_output = tmp_path / f"{output_name}.csv"
    run(input_data_path, output_directory=tmp_path, output_name=output_name)

    assert tmp_output.is_file()

    assert filecmp.cmp(tmp_output, output_data_path)


@pytest.mark.skip(
    reason=r"Plotting is not 100% consistent on different systems, so manual checking is required"
)
def test_create_optical_density_histograms_plot(
    input_data_path: pd.DataFrame, output_histograms_path: Path, tmp_path
) -> None:
    output_name = "output"
    tmp_output = tmp_path / output_histograms_path.name

    run(input_data_path, output_directory=tmp_path, output_name=output_name)

    assert tmp_output.is_file()

    assert filecmp.cmp(tmp_output, output_histograms_path, shallow=False)


@pytest.mark.skip(
    reason=r"Plotting is not 100% consistent on different systems, so manual checking is required"
)
def test_create_optical_density_boxplot_plot(
    input_data_path: pd.DataFrame, output_boxplot_path: Path, tmp_path
) -> None:
    output_name = "output"
    tmp_output = tmp_path / output_boxplot_path.name

    run(input_data_path, output_directory=tmp_path, output_name=output_name)

    assert tmp_output.is_file()

    assert filecmp.cmp(tmp_output, output_boxplot_path, shallow=False)

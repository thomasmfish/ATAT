from pathlib import Path
import pandas as pd
import numpy as np

__example_data_dir = Path(__file__).parent / "example_data"
__input_data_filename = "input_data.csv"
__output_data_filename = "output_data.csv"
__output_histograms_filename = "output_histograms.png"
__output_boxplot_filename = "output_boxplot.png"


def get_example_data_directory() -> Path:
    return __example_data_dir


def get_input_data_path() -> Path:
    return get_example_data_directory() / __input_data_filename


def get_output_data_path() -> Path:
    return get_example_data_directory() / __output_data_filename


def get_output_histograms_path() -> Path:
    return get_example_data_directory() / __output_histograms_filename


def get_output_boxplot_path() -> Path:
    return get_example_data_directory() / __output_boxplot_filename


def create_dataframe_with_duplicate(
    same_optical_density: bool, same_amino_acid_sequence: bool
) -> tuple[pd.DataFrame, pd.DataFrame]:
    row_index = 2
    columns = ["index", "optical_density", "amino_acid_sequence"]
    test_data = np.asarray(
        [
            ["A02", 1.3, "GFTFSNYA"],
            ["A03", 1.3, "GFTFSSYW"],
            ["A04", 0.9, "GFPFEMYD"],
            ["A05", 0.4, "GFTFDDYA"],
        ],
        dtype=np.object_,
    )

    duplicate_row = test_data[row_index, :].copy()
    if not same_optical_density:
        duplicate_row[1] = duplicate_row[1] + 0.2

    if not same_amino_acid_sequence:
        duplicate_row[2] = "ABCDEFGH"  #

    duplicate_test_data = np.vstack((test_data, duplicate_row))

    return pd.DataFrame(duplicate_test_data, columns=columns), pd.DataFrame(
        np.asarray(test_data)[:, 1:], columns=columns[1:]
    )

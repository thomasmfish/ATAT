from pandas.testing import assert_frame_equal

import pandas as pd

import atat

from .utils import get_input_data_path, get_output_data_path

INPUT_DATA_PATH = get_input_data_path()
OUTPUT_DATA_PATH = get_output_data_path()


def test_analyse_statistics():
    input_data = pd.read_csv(INPUT_DATA_PATH)

    output_data = atat.analyse_statistics(input_data)

    expected_output_data = pd.read_csv(OUTPUT_DATA_PATH)

    assert_frame_equal(output_data, expected_output_data)

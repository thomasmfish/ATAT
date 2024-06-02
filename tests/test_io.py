from pandas.testing import assert_frame_equal
import filecmp

import os
from pathlib import Path
from uuid import uuid4
import pandas as pd
from tempfile import gettempdir

from atat import file_handling

from .utils import get_input_data_path, get_output_data_path

INPUT_DATA_PATH = get_input_data_path()
OUTPUT_DATA_PATH = get_output_data_path()


def test_reads_input():
    input_data = file_handling.read_input(INPUT_DATA_PATH)

    expected_input_data = pd.read_csv(INPUT_DATA_PATH)

    assert_frame_equal(input_data, expected_input_data)


def test_saves_output():
    output_data = pd.read_csv(OUTPUT_DATA_PATH)

    tmpfile = Path(gettempdir()) / f"test_saves_output_{uuid4()}"
    try:
        file_handling.save_data(tmpfile, output_data, shallow=False)
        assert filecmp.cmp(tmpfile, OUTPUT_DATA_PATH), "Output files do not match"
    finally:
        os.unlink(tmpfile)


def test_writes_decimal_places(): ...

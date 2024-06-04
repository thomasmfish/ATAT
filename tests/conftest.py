from __future__ import annotations
import pytest

import os
from pathlib import Path
from uuid import uuid4
from tempfile import gettempdir, TemporaryDirectory
import pandas as pd
from typing import TYPE_CHECKING

from .utils import get_input_data_path, get_output_data_path, get_output_plot_path

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture(scope="session")
def input_data_path() -> Path:
    return get_input_data_path()


@pytest.fixture(scope="session")
def output_data_path() -> Path:
    return get_output_data_path()


@pytest.fixture(scope="session")
def output_plot_path() -> Path:
    return get_output_plot_path()


@pytest.fixture(scope="function")
def temporary_file_path() -> Generator[Path, None, None]:
    temporary_path = Path(gettempdir()) / f"ATAT_test_file_{uuid4()}"
    yield temporary_path
    os.unlink(temporary_path)


@pytest.fixture(scope="function")
def temporary_directory() -> Generator[Path, None, None]:
    with TemporaryDirectory(prefix="ATAT_test_dir_") as tmpdir:
        yield Path(tmpdir)


@pytest.fixture(scope="function")
def input_dataframe(input_data_path) -> pd.DataFrame:
    return pd.read_csv(input_data_path)


@pytest.fixture(scope="function")
def output_dataframe(output_data_path) -> pd.DataFrame:
    return pd.read_csv(output_data_path)

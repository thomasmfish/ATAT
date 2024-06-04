from __future__ import annotations

import pandas as pd

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from os import PathLike


def read_input(file_path: str | PathLike[str]) -> pd.DataFrame: ...

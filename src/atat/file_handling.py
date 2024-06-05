from __future__ import annotations

import pandas as pd

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from os import PathLike
    from matplotlib.figure import Figure


def read_input(file_path: str | PathLike[str]) -> pd.DataFrame:
    return pd.read_csv(file_path)


def save_dataframe(file_path: str | PathLike[str], dataframe: pd.DataFrame) -> None:
    dataframe.to_csv(file_path, index=False, lineterminator="\n")


def save_figure(file_path: str | PathLike[str], figure: Figure) -> None:
    figure.savefig(file_path)

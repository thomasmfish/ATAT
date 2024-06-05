from __future__ import annotations
import logging
import pandas as pd

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from os import PathLike
    from matplotlib.figure import Figure

logger = logging.getLogger(__name__)


def read_input(file_path: str | PathLike[str]) -> pd.DataFrame:
    logger.debug("Reading %s", file_path)
    return pd.read_csv(file_path)


def save_dataframe(file_path: str | PathLike[str], dataframe: pd.DataFrame) -> None:
    if file_path.exists():
        raise FileExistsError(f"{file_path} already exists")
    logger.debug("Saving dataframe to %s", file_path)
    dataframe.to_csv(file_path, index=False, lineterminator="\n")


def save_figure(file_path: str | PathLike[str], figure: Figure) -> None:
    if file_path.exists():
        raise FileExistsError(f"{file_path} already exists")
    logger.debug("Saving figure to %s", file_path)
    figure.savefig(file_path)

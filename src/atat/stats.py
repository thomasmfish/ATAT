from __future__ import annotations
from typing import TYPE_CHECKING
import logging

if TYPE_CHECKING:
    import pandas as pd

logger = logging.getLogger(__name__)


def remove_duplicates(dataframe: pd.DataFrame) -> pd.DataFrame: ...

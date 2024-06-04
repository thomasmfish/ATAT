from __future__ import annotations
from typing import TYPE_CHECKING
import logging

import pandas as pd

from .exceptions import DuplicateIndexError

if TYPE_CHECKING:
    from collections.abc import Collection

    from pandas.core.groupby import DataFrameGroupBy

logger = logging.getLogger(__name__)


def analyse_statistics(
    dataframe: pd.DataFrame,
    aa_sequence_column: str = "amino_acid_sequence",
    stat_names: Collection[str] = ("mean", "max", "min"),
    sort: bool = True,
    decimal_places: int = 1,
) -> pd.DataFrame:
    """
    Runs analysis by (in order):
    - Handling/removing duplicate entries
    - Grouping by amino acid sequence
    - Getting analysis output (based on stat_names)
    - Rounding to decimal_places
    - Sorting data by amino acid sequence
    """
    analysed_dataframe = get_statistics_from_grouped_dataframe(
        group_dataframe_by_amino_acid_sequence(
            remove_duplicates(dataframe),
            aa_sequence_column=aa_sequence_column,
            sort=sort,
        ),
        stat_names=stat_names,
    ).round(decimals=decimal_places)
    if sort:
        analysed_dataframe.sort_values(by=aa_sequence_column, inplace=True)
    return analysed_dataframe


def remove_duplicates(
    dataframe: pd.DataFrame, index_column: str = "index"
) -> pd.DataFrame:
    duplicated = dataframe.duplicated(keep=False)
    if any(duplicated.values):
        # Give users a warning if there are duplicates
        logger.warning(
            "Data contains duplicate rows (duplicated rows will only be counted once):\n%s",
            dataframe[duplicated],
        )
        dataframe = dataframe.drop_duplicates(keep="first")

    duplicated_indexes = dataframe.duplicated(index_column, keep=False)
    if any(duplicated_indexes.values):
        # Raise
        raise DuplicateIndexError(
            f"Data contains duplicate indexes on rows:\n{dataframe[duplicated_indexes]}",
        )

    # Index column no longer needed after checking for duplicates
    return dataframe.drop(columns=[index_column])


def group_dataframe_by_amino_acid_sequence(
    dataframe: pd.DataFrame,
    aa_sequence_column: str = "amino_acid_sequence",
    sort: bool = True,
) -> DataFrameGroupBy:
    return dataframe.groupby([aa_sequence_column], sort=sort)


def get_statistics_from_grouped_dataframe(
    grouped_dataframe: DataFrameGroupBy,
    stat_names: Collection[str] = ("mean", "max", "min"),
) -> pd.DataFrame:
    # passing stat_names inverted keeps the order:
    dataframe: pd.DataFrame = grouped_dataframe.agg(stat_names)
    # Combine different level columns, joining names
    dataframe.columns = dataframe.columns.map(lambda s: "_".join(s[::-1])).str.strip()
    return dataframe.reset_index()

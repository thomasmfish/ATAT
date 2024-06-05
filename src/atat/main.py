from __future__ import annotations
import logging
from typing import TYPE_CHECKING, Literal, get_args

from . import file_handling, plotting, stats
from .parser import parse_args


if TYPE_CHECKING:
    from os import PathLike

# First value is the default:
SupportedImageType = Literal["PNG", "JPEG", "TIFF"]
SUPPORTED_IMAGE_STRINGS = get_args(SupportedImageType)

logger = logging.getLogger(__name__)


def run(
    input_file: str | PathLike[str],
    output_directory: str | PathLike[str] | None = None,
    output_name: str | None = None,
    decimal_places: int = 1,
    image_type: SupportedImageType = "PNG",
) -> None:
    if output_directory is None:
        # If no output directory is given, use the input directory as the output
        output_directory = input_file.parent
        logger.info(
            "No output directory specified, setting it to: %s", output_directory
        )

    if output_name is None:
        # If no output directory is given, use the input directory as the output
        output_name = input_file.stem
        logger.info("No output name specified, setting it to: %s", output_name)

    input_dataframe = file_handling.read_input(input_file)
    logger.debug("Creating output csv")
    output_dataframe = stats.analyse_statistics(
        input_dataframe, decimal_places=decimal_places
    )
    file_handling.save_dataframe(
        output_directory / f"{output_name}.csv", output_dataframe
    )
    del output_dataframe
    logger.debug("Creating output figures")
    file_handling.save_figure(
        output_directory / f"{output_name}_boxplot.{image_type.lower()}",
        plotting.create_optical_density_boxplot(input_dataframe),
    )
    file_handling.save_figure(
        output_directory / f"{output_name}_histograms.{image_type.lower()}",
        plotting.create_histograms(input_dataframe),
    )


def main(*args) -> None:
    parsed = parse_args(*args, supported_image_types=SUPPORTED_IMAGE_STRINGS)
    run(
        input_file=parsed.input_file,
        output_directory=parsed.output_directory,
        output_name=parsed.output_name,
        decimal_places=parsed.decimal_places,
        image_type=parsed.image_type,
    )

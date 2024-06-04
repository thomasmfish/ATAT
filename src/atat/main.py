from __future__ import annotations

from typing import TYPE_CHECKING, Literal, get_args

if TYPE_CHECKING:
    from os import PathLike

# First value is the default:
SupportedImageType = Literal["PNG", "JPEG", "TIFF"]
SUPPORTED_IMAGE_STRINGS = get_args(SupportedImageType)


def run(
    input_file: str | PathLike[str],
    output_directory: str | PathLike[str],
    output_name: str | None = None,
    decimal_places: int = 1,
    image_type: SupportedImageType = "PNG",
) -> None: ...


def main(*args) -> None: ...

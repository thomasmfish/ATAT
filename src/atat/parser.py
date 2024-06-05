from __future__ import annotations
import argparse
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def parse_args(*args: str, supported_image_types: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="ATAT")
    parser.add_argument("-i", "--input", dest="input_file", required=True)
    parser.add_argument("-o", "--output-directory", dest="output_directory")
    parser.add_argument("-n", "--output-name")
    parser.add_argument("-dp", "--decimals", dest="decimal_places", type=int, default=1)
    parser.add_argument(
        "-im",
        "--image-type",
        choices=supported_image_types,
        default=supported_image_types[0],
    )

    return parser.parse_args(args)

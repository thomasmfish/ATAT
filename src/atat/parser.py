import argparse
from typing import Any


def parse_args(*args: str) -> dict[str:Any]:
    parser = argparse.ArgumentParser(prog="ATAT")
    parser.add_argument("input_file", nargs="?")
    parser.add_argument("-i", "--input", dest="input_file")
    parser.add_argument("output_directory", nargs="?")
    parser.add_argument("-o", "--output-directory", dest="output_directory")
    parser.add_argument("-n", "--output-name")
    parser.add_argument("-dp", "--decimals", dest="decimal_places")
    parser.add_argument("-im", "--image-type")
    parser.add_argument("--version", action="store_true")

    return vars(parser.parse_args(args))

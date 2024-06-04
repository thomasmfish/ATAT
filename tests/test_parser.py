from typing import Literal
import pytest

from atat import parser


def test_parses_version_arg() -> None:
    assert parser.parse_args("--version")["version"]


def test_requires_input() -> None:
    with pytest.raises(Exception):
        assert parser.parse_args()


@pytest.mark.parametrize(
    "argstring",
    ["--input", "-i", ""],
    ids=["long argname", "short argname", "positional"],
)
def test_accepts_input(argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    args = [argstring, input_value]
    assert parser.parse_args(args)["input_file"] == input_value


@pytest.mark.parametrize(
    "argstring",
    ["--output-directory", "-o", ""],
    ids=["long argname", "short argname", "positional"],
)
def test_set_output_directory(
    argstring: Literal["--output-directory"] | Literal["-o"],
) -> None:
    input_value = "an/input/path/to/file.ext"
    output_directory_value = "an/output/path/"
    args = ["--input", input_value, argstring, output_directory_value]
    assert parser.parse_args(args)["output_directory"] == output_directory_value


@pytest.mark.parametrize(
    "argstring",
    ["--output-name", "-n"],
    ids=["long argname", "short argname"],
)
def test_set_output_name(argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    output_name = "output_name"
    args = ["--input", input_value, argstring, output_name]
    assert parser.parse_args(args)["output_name"] == output_name


@pytest.mark.parametrize(
    "argstring",
    ["--decimals", "-dp"],
    ids=["long argname", "short argname"],
)
def test_set_decimal_places(argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    decimal_places = 7
    args = ["--input", input_value, argstring, decimal_places]
    assert parser.parse_args(args)["decimal_places"] == decimal_places


@pytest.mark.parametrize(
    "argstring",
    ["--image-type", "-im"],
    ids=["long argname", "short argname"],
)
def test_set_image_type(argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    image_type = "image_type"
    args = ["--input", input_value, argstring, image_type]
    assert parser.parse_args(args)["image_type"] == image_type

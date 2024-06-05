from typing import Literal
import pytest

from functools import partial

from atat import parser
from atat.main import SUPPORTED_IMAGE_STRINGS


parse_args_function = partial(
    parser.parse_args, supported_image_types=SUPPORTED_IMAGE_STRINGS
)


def test_requires_input() -> None:
    with pytest.raises(SystemExit):
        assert parse_args_function() is None


@pytest.mark.parametrize(
    "argstring",
    ["--input", "-i"],
    ids=["long argname", "short argname"],
)
def test_accepts_input(argstring) -> None:
    input_file = "an/input/path/to/file.ext"
    args = [argstring, input_file]
    returned_kwargs = parse_args_function(*args)
    assert returned_kwargs.input_file == input_file, f"args are: {returned_kwargs}"


@pytest.mark.parametrize(
    "argstring",
    ["--output-directory", "-o"],
    ids=["long argname", "short argname"],
)
def test_set_output_directory(
    argstring,
) -> None:
    input_value = "an/input/path/to/file.ext"
    output_directory = "an/output/path/"
    args = ["--input", input_value, argstring, output_directory]
    returned_kwargs = parse_args_function(*args)
    assert (
        returned_kwargs.output_directory == output_directory
    ), f"args are: {returned_kwargs}"


@pytest.mark.parametrize(
    "argstring",
    ["--output-name", "-n"],
    ids=["long argname", "short argname"],
)
def test_set_output_name(argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    output_name = "output_name"
    args = ["--input", input_value, argstring, output_name]
    returned_kwargs = parse_args_function(*args)
    assert returned_kwargs.output_name == output_name, f"args are: {returned_kwargs}"


@pytest.mark.parametrize(
    "argstring",
    ["--decimals", "-dp"],
    ids=["long argname", "short argname"],
)
def test_set_decimal_places(argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    decimal_places = 7
    args = ["--input", input_value, argstring, str(decimal_places)]
    returned_kwargs = parse_args_function(*args)
    assert (
        returned_kwargs.decimal_places == decimal_places
    ), f"args are: {returned_kwargs}"


@pytest.mark.parametrize("image_type", SUPPORTED_IMAGE_STRINGS)
@pytest.mark.parametrize(
    "argstring",
    ["--image-type", "-im"],
    ids=["long argname", "short argname"],
)
def test_set_image_type(argstring, image_type) -> None:
    input_value = "an/input/path/to/file.ext"
    args = ["--input", input_value, argstring, image_type]
    returned_kwargs = parse_args_function(*args)
    assert returned_kwargs.image_type == image_type, f"args are: {returned_kwargs}"


def test_set_image_type_default() -> None:
    input_value = "an/input/path/to/file.ext"
    args = ["--input", input_value]
    returned_kwargs = parse_args_function(*args)
    assert (
        returned_kwargs.image_type == SUPPORTED_IMAGE_STRINGS[0]
    ), f"args are: {returned_kwargs}"

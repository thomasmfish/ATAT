import pytest
from unittest.mock import patch

import shlex

from atat.main import main, SUPPORTED_IMAGE_STRINGS


@pytest.mark.parametrize(
    "argstring",
    ["--input", "-i"],
    ids=["long argname", "short argname"],
)
@patch("atat.main.run")
def test_accepts_input(mock_run, argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    main(*shlex.split(f"{argstring} {input_value}"))
    mock_run.assert_called_once_with(
        input_file=input_value,
        output_directory=None,
        output_name=None,
        decimal_places=1,
        image_type="PNG",
    )


@pytest.mark.parametrize(
    "argstring",
    ["--output-directory", "-o"],
    ids=["long argname", "short argname"],
)
@patch("atat.main.run")
def test_set_output_directory(mock_run, argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    output_directory_value = "an/output/path/"
    main(*shlex.split(f"--input {input_value}  {argstring} {output_directory_value}"))
    mock_run.assert_called_once_with(
        input_file=input_value,
        output_directory=output_directory_value,
        output_name=None,
        decimal_places=1,
        image_type="PNG",
    )


@pytest.mark.parametrize(
    "argstring",
    ["--output-name", "-n"],
    ids=["long argname", "short argname"],
)
@patch("atat.main.run")
def test_set_output_name(mock_run, argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    output_name = "output_name"
    main(*shlex.split(f"--input {input_value} {argstring} {output_name}"))
    mock_run.assert_called_once_with(
        input_file=input_value,
        output_directory=None,
        output_name=output_name,
        decimal_places=1,
        image_type="PNG",
    )


@pytest.mark.parametrize(
    "argstring",
    ["--decimals", "-dp"],
    ids=["long argname", "short argname"],
)
@patch("atat.main.run")
def test_set_decimal_places(mock_run, argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    decimal_places = 7
    main(*shlex.split(f"--input {input_value} {argstring} {decimal_places}"))
    mock_run.assert_called_once_with(
        input_file=input_value,
        output_directory=None,
        output_name=None,
        decimal_places=decimal_places,
        image_type="PNG",
    )


@pytest.mark.parametrize("image_type", SUPPORTED_IMAGE_STRINGS)
@pytest.mark.parametrize(
    "argstring",
    ["--image-type", "-im"],
    ids=["long argname", "short argname"],
)
@patch("atat.main.run")
def test_set_image_type(mock_run, argstring, image_type) -> None:
    input_value = "an/input/path/to/file.ext"
    main(*shlex.split(f"--input {input_value} {argstring} {image_type}"))
    mock_run.assert_called_once_with(
        input_file=input_value,
        output_directory=None,
        output_name=None,
        decimal_places=1,
        image_type=image_type,
    )

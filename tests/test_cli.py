from typing import Literal
import pytest
from unittest.mock import patch

from subprocess import Popen, PIPE, DEVNULL

from atat import __version__


def test_displays_version() -> None:
    p = Popen("atat --version", stdout=PIPE, stderr=DEVNULL, text=True)
    p.start()
    stdout, _ = p.communicate(timeout=2)
    assert f"ATAT {__version__}" in stdout


@pytest.mark.parametrize(
    "argstring",
    ["--input", "-i", ""],
    ids=["long argname", "short argname", "positional"],
)
@patch("atat.run")
def test_accepts_input(mock_run, argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    p = Popen(f"atat {argstring} {input_value}", stdout=PIPE, stderr=DEVNULL, text=True)
    p.start()
    p.wait(timeout=2)
    mock_run.assert_called_once_with(input_file=input_value)


@pytest.mark.parametrize(
    "argstring",
    ["--output-directory", "-o", ""],
    ids=["long argname", "short argname", "positional"],
)
@patch("atat.run")
def test_set_output_directory(
    mock_run, argstring: Literal["--output-directory"] | Literal["-o"]
) -> None:
    input_value = "an/input/path/to/file.ext"
    output_directory_value = "an/output/path/"
    p = Popen(
        f"atat --input {input_value}  {argstring} {output_directory_value}",
        stdout=PIPE,
        stderr=DEVNULL,
        text=True,
    )
    p.start()
    p.wait(timeout=2)
    mock_run.assert_called_once_with(
        input_file=input_value, output_directory=output_directory_value
    )


@pytest.mark.parametrize(
    "argstring",
    ["--output-name", "-n"],
    ids=["long argname", "short argname"],
)
@patch("atat.run")
def test_set_output_name(mock_run, argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    output_name = "output_name"
    p = Popen(
        f"atat --input {input_value} {argstring} {output_name}",
        stdout=PIPE,
        stderr=DEVNULL,
        text=True,
    )
    p.start()
    p.wait(timeout=2)
    mock_run.assert_called_once_with(input_file=input_value, output_name=output_name)


@pytest.mark.parametrize(
    "argstring",
    ["--decimals", "-dp"],
    ids=["long argname", "short argname"],
)
@patch("atat.run")
def test_set_decimal_places(mock_run, argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    decimal_places = 7
    p = Popen(
        f"atat --input {input_value} {argstring} {decimal_places}",
        stdout=PIPE,
        stderr=DEVNULL,
        text=True,
    )
    p.start()
    p.wait(timeout=2)
    mock_run.assert_called_once_with(
        input_file=input_value, decimal_places=decimal_places
    )


@pytest.mark.parametrize(
    "argstring",
    ["--image-type", "-im"],
    ids=["long argname", "short argname"],
)
@patch("atat.run")
def test_set_image_type(mock_run, argstring) -> None:
    input_value = "an/input/path/to/file.ext"
    image_type = "image_type"
    p = Popen(
        f"atat --input {input_value} {argstring} {image_type}",
        stdout=PIPE,
        stderr=DEVNULL,
        text=True,
    )
    p.start()
    p.wait(timeout=2)
    mock_run.assert_called_once_with(input_file=input_value, image_type=image_type)

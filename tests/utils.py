from pathlib import Path

__example_data_dir = Path(__file__).parent / "example_data"
__input_data_filename = "input_data.csv"
__output_data_filename = "output_data.csv"


def get_example_data_directory() -> Path:
    return __example_data_dir


def get_input_data_path() -> Path:
    return get_example_data_directory() / __input_data_filename


def get_output_data_path() -> Path:
    return get_example_data_directory() / __output_data_filename

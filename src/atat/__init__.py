import sys

from .version import __version__  # noqa: F401
from .main import main as main_function

if __name__ == "__main__":
    main_function(sys.argv[1:])

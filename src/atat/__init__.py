import sys

from .version import __version__  # noqa: F401
from .main import main

if __name__ == "__main__":
    main(sys.argv[1:])

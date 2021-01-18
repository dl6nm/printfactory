import pathlib

import pytest

from printfactory.print_file import PrintFile


class TestPrintFile:
    """Test PrintFile"""

    print_file = PrintFile(
        file=pathlib.Path(),
    )

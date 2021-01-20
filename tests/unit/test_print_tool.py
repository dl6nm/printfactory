import pathlib

import pytest

from printfactory import Printer, PrintTool


@pytest.mark.parametrize(
    argnames=['name', 'printer', 'app_path', 'args'],
    argvalues=[
        ['Generic PrintTool', Printer(), pathlib.Path(), []],
        [
            'Adobe Reader',
            Printer('MyPrinterName', 'MyDriverName', 'MyPortName'),
            pathlib.Path('AcroRd32.exe'),
            ['/t', 'AcroRd32.exe', 'MyPrinterName', 'MyDriverName', 'MyPortName']
        ],
    ],
)
class TestPrintTool:
    """PrintTool test cases"""

    def test_initialization(self, print_tool, name, printer, app_path, args):
        assert print_tool.name == 'Generic PrintTool'
        assert isinstance(print_tool.printer, Printer)
        assert isinstance(print_tool.app_path, pathlib.Path)
        assert isinstance(print_tool.args, list)

    def test_get_args(self, print_tool, name, printer, app_path, args):
        pta = print_tool.get_args()
        assert isinstance(pta, list)

    @pytest.mark.parametrize(
        argnames='new_args',
        argvalues=[
            ['--verbose', 1, 2],
            ['-v', '--debug'],
        ],
    )
    def test_set_args(self, print_tool, name, printer, app_path, args, new_args):
        pta = print_tool.set_args(new_args)
        assert isinstance(pta, list)

        num_args = len(args) + len(new_args)
        assert len(pta) == num_args

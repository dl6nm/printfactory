import pathlib

import pytest

from printfactory import Printer, PrintTool


@pytest.mark.parametrize(
    argnames=['name', 'printer', 'app_path', 'args', 'exists'],
    argvalues=[
        ['Generic PrintTool', Printer(), pathlib.Path(), [], True],
        [
            'Adobe Reader',
            Printer('MyPrinterName', 'MyDriverName', 'MyPortName'),
            pathlib.Path(r'\path\to\AcroRd32.exe'),
            ['/t', 'AcroRd32.exe', 'MyPrinterName', 'MyDriverName', 'MyPortName'],
            False,
        ],
    ],
)
class TestPrintTool:
    """PrintTool test cases"""

    def test_initialization(self, print_tool, name, printer, app_path, args, exists):
        assert isinstance(print_tool.name, str)
        assert isinstance(print_tool.printer, Printer)
        assert isinstance(print_tool.app_path, pathlib.Path)
        assert isinstance(print_tool.args, list)

    def test_attributes(self, print_tool, name, printer, app_path, args, exists):
        assert print_tool.name == name
        assert print_tool.printer == printer
        assert print_tool.app_path == app_path
        assert print_tool.args == args

    def test_exists(self, print_tool, name, printer, app_path, args, exists):
        assert print_tool.exists() == exists

    def test_get_args(self, print_tool, name, printer, app_path, args, exists):
        print_tool_args = print_tool.get_args()
        assert isinstance(print_tool_args, list)
        assert print_tool_args == args

    @pytest.mark.parametrize(
        argnames='new_args',
        argvalues=[
            ['--verbose', 1, 2],
        ],
    )
    def test_set_args(self, print_tool, name, printer, app_path, args, exists, new_args):
        print_tool_args = print_tool.set_args(new_args)
        assert isinstance(print_tool_args, list)
        assert len(print_tool_args) == len(new_args)

    @pytest.mark.parametrize(
        argnames='print_file',
        argvalues=[
            ['my.pdf'],
        ],
    )
    def test_print_file(self, print_tool, name, printer, app_path, args, exists, print_file):
        assert print_tool.print_file(print_file) is True

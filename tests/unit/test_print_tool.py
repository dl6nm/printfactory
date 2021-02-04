import pathlib
import subprocess

import pytest

from printfactory import Printer, PrintTool


@pytest.mark.parametrize(
    argnames=['name', 'printer', 'app_path', 'args', 'exists'],
    argvalues=[
        [
            'Adobe Reader',
            Printer('MyPrinterName', 'MyDriverName', 'MyPortName'),
            pathlib.Path(r'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'),
            ['/t', 'MyPrintFile.pdf', 'MyPrinterName', 'MyDriverName', 'MyPortName'],
            True,
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
        argnames='add_args',
        argvalues=[
            ['--printer', 'MyPrinter', '--port', '1234'],
        ],
    )
    def test_add_args(self, print_tool, name, printer, app_path, args, exists, add_args):
        total_args = len(args) + len(add_args)
        print_tool_args = print_tool.add_args(add_args)
        assert isinstance(print_tool_args, list)
        assert len(print_tool_args) == total_args
        assert len(print_tool.get_args()) == total_args

    # @pytest.mark.parametrize(
    #     argnames='print_file',
    #     argvalues=[
    #         ['my.pdf'],
    #     ],
    # )
    # def test_print_file(self, print_tool, name, printer, app_path, args, exists, print_file):
    #     print_tool.set_args(args)
    #     assert print_tool.print_file(print_file) is True


@pytest.mark.parametrize(
    argnames=['name', 'printer', 'app_path', 'args'],
    argvalues=[
        ['Generic PrintTool', Printer(), pathlib.Path(), []],
    ],
)
class TestPrintToolFail:
    """PrintTool test cases - Failing tests"""

    def test_initialization_fail(self, name, printer, app_path, args):
        with pytest.raises(FileNotFoundError) as execinfo:
            PrintTool(name, printer, app_path, args)
        assert execinfo.value.args[0] == 'PrintTool "." does not exist'

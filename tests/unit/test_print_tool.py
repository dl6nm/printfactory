import pathlib

import pytest

from printfactory import Printer, PrintTool


@pytest.mark.parametrize(
    argnames=['print_tool_name', 'name', 'printer', 'app_path', 'args', 'exists'],
    argvalues=[
        [
            'AdobeReader',
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

    def test_initialization(self, print_tool, print_tool_name, name, printer, app_path, args, exists):
        assert isinstance(print_tool.name, str)
        assert isinstance(print_tool.printer, Printer)
        assert isinstance(print_tool.app_path, pathlib.Path)
        assert isinstance(print_tool.args, list)

    def test_attributes(self, print_tool, print_tool_name, name, printer, app_path, args, exists):
        assert print_tool.name == name
        assert print_tool.printer == printer
        assert print_tool.app_path == app_path
        assert print_tool.args == args

    def test_exists(self, print_tool, print_tool_name, name, printer, app_path, args, exists):
        assert print_tool.exists() == exists

    def test_get_args(self, print_tool, print_tool_name, name, printer, app_path, args, exists):
        print_tool_args = print_tool.get_args()
        assert isinstance(print_tool_args, list)
        assert print_tool_args == args

    @pytest.mark.parametrize(
        argnames='new_args',
        argvalues=[
            ['--verbose', 1, 2],
        ],
    )
    def test_set_args(self, print_tool, print_tool_name, name, printer, app_path, args, exists, new_args):
        print_tool_args = print_tool.set_args(new_args)
        assert isinstance(print_tool_args, list)
        assert len(print_tool_args) == len(new_args)

    @pytest.mark.parametrize(
        argnames='add_args',
        argvalues=[
            ['--printer', 'MyPrinter', '--port', '1234'],
        ],
    )
    def test_add_args(self, print_tool, print_tool_name, name, printer, app_path, args, exists, add_args):
        total_args = len(args) + len(add_args)
        print_tool_args = print_tool.add_args(add_args)
        assert isinstance(print_tool_args, list)
        assert len(print_tool_args) == total_args
        assert len(print_tool.get_args()) == total_args

    def test_string_representation(self, print_tool, print_tool_name, name, printer, app_path, args, exists):
        expected_str = f'{print_tool.__class__.__name__}(printer={print_tool.printer}, ' \
                       f'app_path="{print_tool.app_path}", args={print_tool.args}, ' \
                       f'name="{print_tool.name}", timeout={print_tool.timeout})'
        assert str(print_tool) == expected_str


@pytest.mark.parametrize(
    argnames=['printer', 'app_path', 'args', 'name'],
    argvalues=[
        [Printer(), pathlib.Path(), [], 'Generic PrintTool'],
    ],
)
class TestPrintToolFail:
    """PrintTool test cases - Failing tests"""

    def test_initialization_fail(self, printer, app_path, args, name):
        with pytest.raises(FileNotFoundError) as execinfo:
            PrintTool(printer=printer, app_path=app_path, args=args, name=name)
        assert execinfo.value.args[0] == 'PrintTool "." does not exist'
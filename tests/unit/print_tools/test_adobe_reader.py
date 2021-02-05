import pathlib

import pytest

from printfactory import AdobeReader, Printer, PrintTool


@pytest.fixture()
def reader(printer):
    return AdobeReader(
        printer=printer,
    )


@pytest.mark.parametrize(
    argnames='printer',
    argvalues=[
        Printer('BlackHole', 'MyDriverName', 'MyPortName'),
    ],
)
class TestAdobeReader:
    """Adobe Reader class tests"""

    @pytest.mark.parametrize(
        argnames=['name', 'app_path'],
        argvalues=[
            [
                'Adobe Reader',
                pathlib.Path(r'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'),
            ],
        ],
    )
    def test_initialization(self, printer, reader, name, app_path):
        assert isinstance(reader, PrintTool)
        assert reader.exists() is True
        assert reader.name == name
        assert reader.printer == printer
        assert reader.app_path == app_path
        assert reader.args == []

    @pytest.mark.parametrize(
        argnames=['print_file_name', 'args_expected'],
        argvalues=[
            [
                'my.pdf',
                ['/t', '{print_file}', 'BlackHole', 'MyDriverName', 'MyPortName'],
            ],
        ],
    )
    def test__set_args(self, printer, reader, print_file_name, args_expected, shared_datadir):
        print_file = shared_datadir / print_file_name

        # replace {print_file} placeholder with real print_file path
        for arg in range(len(args_expected)):
            if args_expected[arg] == '{print_file}':
                args_expected[arg] = print_file

        assert reader._set_args(print_file=print_file) == args_expected
        assert reader.get_args() == args_expected

    @pytest.mark.parametrize(
        argnames=['print_file_name', 'success'],
        argvalues=[
            ['my.pdf', True],
            ['no-file.pdf', False],
        ],
    )
    def test_print_file(self, printer, reader, print_file_name, success, shared_datadir):
        print_file = shared_datadir / print_file_name
        assert reader.print_file(file=print_file) is success

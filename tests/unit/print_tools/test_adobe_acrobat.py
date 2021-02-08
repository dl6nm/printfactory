import pathlib

import pytest

from printfactory import AdobeAcrobat, Printer, PrintTool


@pytest.fixture()
def acrobat(printer):
    return AdobeAcrobat(
        printer=printer,
    )


@pytest.mark.parametrize(
    argnames='printer',
    argvalues=[
        Printer('BlackHole', None, None),
    ],
)
class TestAdobeAcrobat:
    """Adobe Acrobat class tests"""

    @pytest.mark.parametrize(
        argnames=['name', 'app_path'],
        argvalues=[
            [
                'Adobe Acrobat',
                pathlib.Path(r'C:\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Acrobat.exe'),
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
                ['/n', '/t', '{print_file}', 'BlackHole'],
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
        argnames=['print_file_name', 'success', 'raises'],
        argvalues=[
            ['my.pdf', True, None],
            ['no-file.pdf', False, FileNotFoundError],
        ],
    )
    def test_print_file(self, printer, reader, print_file_name, success, raises, shared_datadir):
        print_file = shared_datadir / print_file_name
        if success:
            printed = reader.print_file(file=print_file)
            assert printed is success
        else:
            with pytest.raises(raises) as execinfo:
                reader.print_file(file=print_file)
            assert execinfo.value.args[0].endswith('does not exist')

import pathlib

import pytest

from printfactory import AdobeReader, Printer, PrintTool


@pytest.mark.parametrize(
    argnames=['print_tool_name', 'name', 'printer', 'app_path', 'args'],
    argvalues=[
        [
            'AdobeReader',
            'Adobe Reader',
            Printer('BlackHole', None, None),
            pathlib.Path(r'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'),
            None,
        ],
        [
            'AdobeAcrobat',
            'Adobe Acrobat',
            Printer('BlackHole', None, None),
            pathlib.Path(r'C:\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Acrobat.exe'),
            None,
        ],
    ],
    ids=[
        'AdobeReader',
        'AdobeAcrobat',
    ]
)
class TestAdobe:
    """AdobeReader and AdobeAcrobat class tests"""

    def test_initialization(self, printer, print_tool, print_tool_name, name, app_path, args):
        assert isinstance(print_tool, PrintTool)
        assert isinstance(print_tool, AdobeReader)
        assert print_tool.exists() is True
        assert print_tool.name == name
        assert print_tool.printer == printer
        assert print_tool.app_path == app_path
        assert print_tool.args is None

    @pytest.mark.parametrize(
        argnames=['print_file_name', 'args_expected'],
        argvalues=[
            [
                'my.pdf',
                ['/n', '/t', '{print_file}', 'BlackHole'],
            ],
        ],
    )
    def test__set_args(self, printer, print_tool, name, print_file_name, args_expected, shared_datadir):
        print_file = shared_datadir / print_file_name

        # replace {print_file} placeholder with real print_file path
        for arg in range(len(args_expected)):
            if args_expected[arg] == '{print_file}':
                args_expected[arg] = print_file

        assert print_tool._set_args(print_file=print_file) == args_expected
        assert print_tool.get_args() == args_expected

    @pytest.mark.parametrize(
        argnames=['print_file_name', 'success', 'raises'],
        argvalues=[
            ['my.pdf', True, None],
            ['no-file.pdf', False, FileNotFoundError],
        ],
    )
    def test_print_file(self, printer, print_tool, name, print_file_name, success, raises, shared_datadir):
        print_file = shared_datadir / print_file_name
        if success:
            printed = print_tool.print_file(file=print_file)
            assert printed is success
        else:
            with pytest.raises(raises) as execinfo:
                print_tool.print_file(file=print_file)
            assert execinfo.value.args[0].endswith('does not exist')

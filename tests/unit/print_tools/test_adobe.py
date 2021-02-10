import pathlib

import pytest

from printfactory import AdobeReader, Printer, PrintTool


@pytest.mark.parametrize(
    argnames=['print_tool_name', 'name', 'printer', 'app_path', 'args', 'args_expected'],
    argvalues=[
        [
            'AdobeReader',
            'Adobe Reader',
            Printer('BlackHole', None, None),
            pathlib.Path(r'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'),
            None,
            ['/n', '/t', '{print_file}', 'BlackHole'],
        ],
        [
            'AdobeAcrobat',
            'Adobe Acrobat',
            Printer('BlackHole', None, None),
            pathlib.Path(r'C:\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Acrobat.exe'),
            None,
            ['/n', '/t', '{print_file}'],
        ],
    ],
    ids=[
        'AdobeReader',
        'AdobeAcrobat',
    ]
)
class TestAdobe:
    """AdobeReader and AdobeAcrobat class tests"""

    def test_initialization(
            self, printer, print_tool, print_tool_name, name, app_path, args, args_expected
    ):
        assert isinstance(print_tool, PrintTool)
        assert isinstance(print_tool, AdobeReader)
        assert print_tool.exists() is True
        assert print_tool.name == name
        assert print_tool.printer == printer
        assert print_tool.app_path == app_path
        assert print_tool.args is None
        assert print_tool.timeout == 60

    @pytest.mark.parametrize(
        argnames=['print_file_name'],
        argvalues=[
            [
                'my.pdf',
            ],
        ],
    )
    def test__set_args(
            self, printer, print_tool, print_tool_name, name, app_path, args, args_expected,
            print_file_name, original_datadir
    ):
        print_file = original_datadir / print_file_name

        # replace {print_file} placeholder with real print_file path
        for arg in range(len(args_expected)):
            if args_expected[arg] == '{print_file}':
                args_expected[arg] = print_file

        assert print_tool._set_args(print_file=print_file) == args_expected
        assert print_tool.get_args() == args_expected

    @pytest.mark.parametrize(
        argnames=['print_file_name', 'raises'],
        argvalues=[
            ['my.pdf', None],
            ['no-file.pdf', FileNotFoundError],
        ],
    )
    def test_print_file(
            self, printer, print_tool, print_tool_name, name, app_path, args, args_expected,
            print_file_name, raises, original_datadir
    ):
        print_file = original_datadir / print_file_name

        if not raises:
            printed = print_tool.print_file(file=print_file)
            assert printed
        else:
            with pytest.raises(raises) as execinfo:
                print_tool.print_file(file=print_file)
            assert execinfo.value.args[0].endswith('does not exist')

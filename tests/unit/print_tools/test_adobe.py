import pathlib

import pytest

from printfactory import AdobeReader, Printer, GenericPrintTool


@pytest.mark.parametrize(
    argnames=['print_tool_name', 'name', 'printer', 'app_path', 'args', 'args_expected'],
    argvalues=[
        [
            'AdobeReader',
            'Adobe Reader',
            Printer(),
            pathlib.Path(r'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'),
            None,
            ['/n', '/t', '{print_file}'],
        ],
        [
            'AdobeAcrobat',
            'Adobe Acrobat',
            Printer(),
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
        assert isinstance(print_tool, GenericPrintTool)
        assert isinstance(print_tool, AdobeReader)
        assert print_tool.exists() is True
        assert print_tool.name == name
        assert print_tool.printer == printer
        assert print_tool.app_path == app_path
        assert print_tool.args is None
        assert print_tool.timeout == 60

    @pytest.mark.parametrize(
        argnames=['print_file_name', 'printer_variation', 'args_expected_printer'],
        argvalues=[
            [
                'my.pdf',
                Printer('BlackHole', None, None),
                ['BlackHole'],
            ],
            [
                'my.pdf',
                Printer('BlackHole', 'Generic / Text Only', None),
                ['BlackHole', 'Generic / Text Only']
            ],
            [
                'my.pdf',
                Printer('BlackHole', 'Generic / Text Only', 'BlackHole'),
                ['BlackHole', 'Generic / Text Only', 'BlackHole']
            ],
        ],
    )
    def test__set_args(
            self, printer, print_tool, print_tool_name, name, app_path, args, args_expected,
            print_file_name, printer_variation, args_expected_printer, original_datadir
    ):
        print_file = original_datadir / print_file_name
        _args_expected = args_expected.copy()

        for arg in range(len(_args_expected)):
            if _args_expected[arg] == '{print_file}':
                _args_expected[arg] = print_file

        # Only AdobeReader has currently support for Printer attributes
        if type(print_tool) == AdobeReader:
            _args_expected.extend(args_expected_printer)
            print_tool.printer = printer_variation

        assert print_tool._set_args(print_file=print_file) == _args_expected
        assert print_tool.get_args() == _args_expected

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

    @pytest.mark.parametrize(
        argnames=['print_file_name', 'copies', 'raises'],
        argvalues=[
            ['my.pdf', None, ValueError],
            ['my.pdf', 0, ValueError],
            ['my.pdf', 'three', ValueError],
            ['my.pdf', 1, None],
            ['my.pdf', 3, None],
        ],
    )
    def test_print_file_copies(
            self, printer, print_tool, print_tool_name, name, app_path, args, args_expected,
            print_file_name, copies, raises, original_datadir
    ):
        print_file = original_datadir / print_file_name

        if not raises:
            printed = print_tool.print_file(file=print_file, copies=copies)
            assert printed
        else:
            with pytest.raises(raises) as execinfo:
                print_tool.print_file(file=print_file, copies=copies)
            assert execinfo.value.args[0].endswith('is not a valid number of copies')

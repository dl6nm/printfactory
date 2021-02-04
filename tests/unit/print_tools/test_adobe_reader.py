import pathlib

import pytest

from printfactory import AdobeReader, Printer, PrintTool


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
class TestAdobeReader:
    """Adobe Reader class tests"""

    def test_initialization(self, name, printer, app_path, args, exists):
        reader = AdobeReader(
            printer=printer,
        )
        assert isinstance(reader, PrintTool)
        assert reader.name == name
        assert reader.printer == printer
        assert reader.app_path == app_path
        assert reader.get_args() == args
        assert reader.exists() is exists


@pytest.mark.parametrize(
    argnames=['name', 'printer', 'app_path', 'args', 'exists'],
    argvalues=[
        [
            'Adobe Reader',
            Printer('MyPrinterName', 'MyDriverName', 'MyPortName'),
            pathlib.Path(),
            ['/t', 'MyPrintFile.pdf', 'MyPrinterName', 'MyDriverName', 'MyPortName'],
            True,
        ],
    ],
)
class TestAdobeReaderFail:
    """Adobe Reader class - Failing tests"""

    def test_initialization(self, name, printer, app_path, args, exists):
        with pytest.raises(FileNotFoundError) as execinfo:
            AdobeReader(
                printer=printer,
            )
        assert execinfo.value.args[0] == 'PrintTool "." does not exist'

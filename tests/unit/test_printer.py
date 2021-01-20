import pytest

from printfactory import Printer


@pytest.mark.parametrize(
    argnames=['printer_name', 'printer_driver', 'printer_port'],
    argvalues=[
        [None, None, None],
        ['MyPrinter', None, None],
        ['MyPrinter', 'MyDriver', None],
        ['MyPrinter', 'MyDriver', 'Portname_1234'],
    ],
)
class TestPrinter:
    """Test Printer class"""

    def test_attributes(self, printer, printer_name, printer_driver, printer_port):
        assert printer.name == printer_name
        assert printer.driver == printer_driver
        assert printer.port == printer_port

    def test_get_list(self, printer, printer_name, printer_driver, printer_port):
        # static method
        printers = Printer.get_list()
        assert len(printer) >= 0
        assert 'BlackHole' in printers

    def test_get_default(self, printer):
        default_printer = Printer.get_default()
        assert len(default_printer) == 1
        assert isinstance(default_printer, Printer)


class TestPrinterFail:
    """Test Printer class - Failing tests"""

    @pytest.mark.parametrize(
        argnames=['printer_name', 'printer_driver', 'printer_port', 'exception_msg'],
        argvalues=[
            [None, 'MyDriverName', None, 'Missing printer'],
            ['MyPrinter', None, 1234, 'Missing driver'],
            [None, 'MyDriverName', 'MyPrinterPort', 'Missing printer'],
            [None, None, 'MyPrinterPort', 'Missing printer'],
        ],
        ids=None,
    )
    def test_fail_missing_attributes(self, printer, printer_name, printer_driver, printer_port, exception_msg):
        with pytest.raises(TypeError) as execinfo:
            printer
        assert execinfo.value.args[0] == exception_msg


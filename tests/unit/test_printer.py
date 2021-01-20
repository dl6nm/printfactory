import pytest

from printfactory import Printer


class TestPrinter:
    """Test Printer class"""

    @pytest.mark.parametrize(
        argnames=['printer_name', 'driver_name', 'port_name'],
        argvalues=[
            [None, None, None],
            ['MyPrinter', None, None],
            ['MyPrinter', 'MyDriver', None],
            ['MyPrinter', 'MyDriver', 'Portname_1234'],
        ],
    )
    def test_attributes(self, printer, printer_name, driver_name, port_name):
        assert printer.name == printer_name
        assert printer.driver == driver_name
        assert printer.port == port_name

    def test_get_list(self):
        # static method
        printers = Printer.get_list()
        assert len(printers) > 0
        assert 'BlackHole' in printers

    def test_get_default(self):
        default_printer = Printer.get_default()
        assert isinstance(default_printer, Printer)
        assert default_printer.name not in [None, '']


class TestPrinterFail:
    """Test Printer class - Failing tests"""

    @pytest.mark.parametrize(
        argnames=['printer_name', 'driver_name', 'port_name', 'exception_msg'],
        argvalues=[
            [None, 'MyDriverName', None, 'Missing printer'],
            ['MyPrinter', None, 1234, 'Missing driver'],
            [None, 'MyDriverName', 'MyPrinterPort', 'Missing printer'],
            [None, None, 'MyPrinterPort', 'Missing printer'],
        ],
        ids=None,
    )
    def test_fail_missing_attributes(self, printer, printer_name, driver_name, port_name, exception_msg):
        with pytest.raises(TypeError) as execinfo:
            printer
        assert execinfo.value.args[0] == exception_msg


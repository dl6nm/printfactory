import pytest

from printfactory import Printer


@pytest.mark.parametrize(
    argnames=['printer_name', 'driver_name', 'port_name', 'default'],
    argvalues=[
        [None, None, None, False],
        ['MyPrinter', None, None, True],
        ['MyPrinter', 'MyDriver', None, False],
        ['MyPrinter', 'MyDriver', 'Portname_1234', True],
    ],
)
class TestPrinter:
    """Test Printer class"""

    def test_attributes(self, printer, printer_name, driver_name, port_name, default):
        printer._default = default  # set printers _default bool value for testing
        assert isinstance(printer.name, (type(None), str))
        assert isinstance(printer.driver, (type(None), str))
        assert isinstance(printer.port, (type(None), str))
        assert isinstance(printer._default, (type(None), bool))

        assert printer.name == printer_name
        assert printer.driver == driver_name
        assert printer.port == port_name
        assert printer._default == default



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
    def test_fail_missing_attributes(self, printer_name, driver_name, port_name, exception_msg):
        with pytest.raises(TypeError) as execinfo:
            Printer(
                printer_name=printer_name,
                driver_name=driver_name,
                port_name=port_name,
            )
        assert execinfo.value.args[0] == exception_msg

class TestPrinterStaticMethods:
    """Test Printer class' static methods"""
    
    def test_get_list(self):
        # static method
        printers = Printer.get_list()
        assert isinstance(printers, list)
        assert len(printers) > 0
        for printer in printers:
            assert isinstance(printer, Printer)

    def test_get_default(self):
        default_printer = Printer.get_default()
        assert isinstance(default_printer, Printer)
        assert default_printer.name not in [None, '']

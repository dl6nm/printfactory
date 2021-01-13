from printfactory.models.print_tools import AdobeAcrobat, AdobeReader

import pytest


@pytest.mark.parametrize(
    argnames=['print_tool_class', 'print_tool_name', 'print_tool_executable', 'print_tool_path'],
    argvalues=[
        [AdobeAcrobat, 'Adobe Acrobat', 'Acrobat.exe', r'\Adobe\Acrobat DC\Acrobat\Acrobat.exe'],
        [AdobeReader, 'Adobe Reader', 'AcroRd32.exe', r'\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe']
    ],
    ids=['AdobeAcrobat', 'AdobeReader']
)
class TestAdobe:

    @pytest.mark.parametrize(
        argnames=['printer_name', 'driver_name', 'port_name'],
        argvalues=[
            [None, None, None],
            ['MyPrinter', None, None],
            ['MyPrinter', 'MyDriverName', None],
            ['MyPrinter', 'MyDriverName', 1234],
            ['MyPrinter', 'MyDriverName', 'MyPrinterPort'],
        ],
        ids=None,
    )
    def test_init(self, print_tool_class, print_tool_name, print_tool_executable, print_tool_path,
                  printer_name, driver_name, port_name):
        printer = print_tool_class(
            printer_name=printer_name,
            driver_name=driver_name,
            port_name=port_name,
        )

        assert printer.name == print_tool_name
        assert print_tool_path in str(printer.app_path)

        assert printer.printer_name is printer_name
        assert printer.driver_name is driver_name
        assert printer.port_name is port_name

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
    def test_init_fail(self, print_tool_class, print_tool_name, print_tool_executable, print_tool_path,
                       printer_name, driver_name, port_name, exception_msg):
        with pytest.raises(TypeError) as execinfo:
            print_tool_class(
                printer_name=printer_name,
                driver_name=driver_name,
                port_name=port_name,
            )
        assert execinfo.value.args[0] == exception_msg

    @pytest.mark.parametrize(
        argnames=['printer_name', 'driver_name', 'port_name', 'print_file_name', 'num_args'],
        argvalues=[
            [None, None, None, 'my.pdf', 3],
            ['MyPrinter', None, None, 'my.pdf', 4],
            ['MyPrinter', 'MyDriverName', None, 'my.pdf', 5],
            ['MyPrinter', 'MyDriverName', 1234, 'my.pdf', 6],
            ['MyPrinter', 'MyDriverName', 'MyPrinterPort', 'my.pdf', 6],
        ],
        ids=None,
    )
    def test_get_args(self, print_tool_class, print_tool_name, print_tool_executable, print_tool_path,
                      datadir, printer_name, driver_name, port_name, print_file_name, num_args):
        printer = print_tool_class(
            printer_name=printer_name,
            driver_name=driver_name,
            port_name=port_name,
        )
        print_file = datadir / print_file_name

        args = printer.get_args(print_file)
        assert type(args) is list
        assert None not in args
        assert len(args) == num_args

        assert print_tool_executable in str(args[0])
        assert '/t' in str(args[1])
        assert args[2] == print_file

        if printer_name:
            assert args[3] == printer_name
        if driver_name:
            assert args[4] == driver_name
        if port_name:
            assert args[5] == port_name

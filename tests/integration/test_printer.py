import pytest

import printfactory

from printfactory.models.print_tools import AdobeAcrobat, AdobeReader


def test_list_printers():
    printers = printfactory.list_printers()
    assert len(printers) > 0


@pytest.mark.parametrize(
    argnames=['printer_name', 'printer_driver', 'printer_port_name', 'print_tool', 'filename'],
    argvalues=[
        ['BlackHole', None, None, AdobeAcrobat, 'my.pdf'],
        ['BlackHole', None, None, AdobeReader, 'my.pdf'],
        ['BlackHole', 'Optional print driver', '1234', AdobeAcrobat, 'my.pdf'],
        ['BlackHole', 'Optional print driver', '1234', AdobeReader, 'my.pdf'],
    ],
)
def test_printer(printer_name, printer_driver, printer_port_name, filename, print_tool, shared_datadir):
    # @todo: Check if BlackHole printer is installed on Windows, of not install it and remove it after the tests
    # @todo: Add print_tool in tests
    printer = printfactory.Printer(
        printer_name=printer_name,
        driver_name=printer_driver,
        port_name=printer_port_name,
        print_tool=print_tool,
    )

    assert printer.name is printer_name
    assert printer.driver is printer_driver
    assert printer.port is printer_port_name
    assert printer.print_tool is print_tool.name

    file = (shared_datadir / filename)
    assert printer.send(file, timeout=10) is None


@pytest.mark.parametrize(
    argnames='filename',
    argvalues=[
        'file-does-not-exist.pdf',
        'file/not/found/my.pdf',
        'directory/',
    ],
)
def test_printer_missing_file(filename, shared_datadir):
    """Fail test on sending a missing file to a printer"""
    printer = printfactory.Printer()
    file = (shared_datadir / filename)
    with pytest.raises(FileNotFoundError):
        printer.send(file, timeout=10)

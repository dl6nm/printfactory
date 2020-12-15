import pytest

import printfactory


@pytest.mark.parametrize(
    argnames=['name', 'driver', 'port', 'filename'],
    argvalues=[
        ['EPSON AL-C2800N', None, None, None],
    ],
    ids=None,
)
def test_printer_windows(name, driver, port, filename):
    printer = printfactory.Printer(
        name=name,
        driver=driver,
        port=port,
    )
    assert printer.name is name
    assert printer.driver is driver
    assert printer.port is port
    assert printer.print_file(filename) is True


def test_list_printers():
    printers = printfactory.list_printers()
    assert 'Fax' in printers

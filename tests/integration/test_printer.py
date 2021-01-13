import pytest

import printfactory


def test_list_printers():
    printers = printfactory.list_printers()
    assert len(printers) > 0


@pytest.mark.parametrize(
    argnames=['name', 'driver', 'port', 'print_tool', 'filename'],
    argvalues=[
        ['BlackHole', None, None, None, 'my.pdf'],
        ['BlackHole', 'Optional print driver', 1234, None, 'my.pdf'],
    ],
)
def test_printer(name, driver, port, filename, print_tool, shared_datadir):
    printer = printfactory.Printer(
        printer_name=name,
        driver_name=driver,
        port_name=port,
        # print_tool=print_tool,
    )

    assert printer.name is name
    assert printer.driver is driver
    assert printer.port is port

    file = (shared_datadir / filename)
    assert printer.send(file, timeout=10) is None

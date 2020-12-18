import pathlib

import pytest

import printfactory


def test_list_printers():
    printers = printfactory.list_printers()
    assert len(printers) > 0


@pytest.mark.parametrize(
    argnames=['name', 'driver', 'port', 'print_tool', 'filename'],
    argvalues=[
        ['Office Printer', None, None, None, 'my.pdf'],
        ['My second printer', 'Optional print driver', 1234, None, 'my.pdf'],
    ],
    ids=None,
)
def test_printer(name, driver, port, filename, print_tool, shared_datadir):
    printer = printfactory.Printer(
        printer_name=name,
        driver_name=driver,
        port_name=port,
        # print_tool=print_tool,
    )

    file = (shared_datadir / filename)

    assert printer.name is name
    assert printer.driver is driver
    assert printer.port is port
    # assert printer.send(file) is True

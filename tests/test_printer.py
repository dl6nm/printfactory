import pathlib

import pytest

import printfactory


@pytest.mark.parametrize(
    argnames=['name', 'driver', 'port', 'filename'],
    argvalues=[
        ['Office Printer', None, None, 'my.pdf'],
        ['My second printer', 'Optional print driver', 1234, 'my.pdf'],
    ],
    ids=None,
)
def test_printer(name, driver, port, filename, datadir):
    printer = printfactory.Printer(
        name=name,
        driver=driver,
        port=port,
        print_tool=None,
    )
    file = pathlib.Path(datadir) / filename

    assert printer.name is name
    assert printer.driver is driver
    assert printer.port is port
    assert printer.print_file(file) is True


def test_list_printers():
    printers = printfactory.list_printers()
    assert len(printers) > 0

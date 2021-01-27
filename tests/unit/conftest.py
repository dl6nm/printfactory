import pytest

from printfactory import Printer, PrintTool


@pytest.fixture()
def printer(printer_name, driver_name, port_name, is_default):
    return Printer(
        printer_name=printer_name,
        driver_name=driver_name,
        port_name=port_name,
        _default=is_default,
    )


@pytest.fixture()
def print_tool(name, printer, app_path, args):
    return PrintTool(
        name=name,
        printer=printer,
        app_path=app_path,
        args=args,
    )

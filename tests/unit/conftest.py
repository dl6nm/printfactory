import pytest

from printfactory import Printer, PrintTool


@pytest.fixture()
def printer(printer_name, driver_name, port_name):
    return Printer(
        printer_name=printer_name,
        driver_name=driver_name,
        port_name=port_name,
    )


@pytest.fixture()
def print_tool(name, printer, app_path, args):
    return PrintTool(
        name=name,
        printer=printer,
        app_path=app_path,
        args=args,
    )

import pytest

from typing import List

from printfactory import Printer


@pytest.fixture()
def printer(printer_name, driver_name, port_name, is_default):
    return Printer(
        printer_name=printer_name,
        driver_name=driver_name,
        port_name=port_name,
        _default=is_default,
    )


@pytest.fixture()
def print_tool(print_tool_name, printer, app_path, args: List[str]):
    module = __import__('printfactory')
    print_tool_instance = getattr(module, print_tool_name)(
        printer=printer,
        app_path=app_path,
        args=args,
    )
    return print_tool_instance

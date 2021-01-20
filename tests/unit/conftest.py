import pytest

from printfactory import Printer


@pytest.fixture()
def printer(printer_name, printer_driver, printer_port):
    return Printer(
        printer_name=printer_name,
        driver_name=printer_driver,
        port_name=printer_port,
    )

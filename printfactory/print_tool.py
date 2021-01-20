import pathlib

from . import Printer


class PrintTool:
    """Generic PrintTool"""

    def __init__(self, name, printer, app_path, args):
        self.name = name
        self.printer = printer
        self.app_path = app_path
        self.args = args

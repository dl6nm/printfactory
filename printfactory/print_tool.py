import pathlib

from typing import List

from . import Printer


class PrintTool:
    """Generic PrintTool"""

    def __init__(self, name, printer, app_path, args):
        self.name: str = name
        self.printer: Printer = printer
        self.app_path: pathlib.Path = app_path
        self.args: List[str] = args

    def exists(self):
        app_path_exists = self.app_path.exists()
        return app_path_exists

    def get_args(self):
        return self.args

    def set_args(self, args):
        self.args = args
        return self.args

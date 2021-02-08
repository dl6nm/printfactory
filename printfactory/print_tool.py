import pathlib
import platform
import subprocess

from typing import List

from . import Printer

PRINTTOOL_TIMEOUT = 60


class PrintTool:
    """Generic PrintTool"""

    def __init__(self, printer: Printer, app_path: pathlib.Path, args: List[str] = None, name: str = 'Generic PrintTool',):
        self.printer = printer
        self.app_path = app_path
        self.args = args
        self.name = name
        self.timeout = PRINTTOOL_TIMEOUT

        if not self.exists():
            raise FileNotFoundError(f'PrintTool "{app_path}" does not exist')

    def exists(self) -> bool:
        if not self.app_path.is_dir():
            return self.app_path.exists()
        return False

    def get_args(self) -> List[str]:
        return self.args

    def set_args(self, args: List[str]) -> List[str]:
        self.args = args
        return self.args

    def add_args(self, args: List[str]) -> List[str]:
        self.args.extend(args)
        return self.args

    def run(self) -> subprocess.CompletedProcess:
        pltfrm = platform.system()
        if pltfrm == 'Windows':
            shell = False
        elif pltfrm == 'Darwin':
            shell = True
        else:
            raise NotImplementedError

        args = [self.app_path.absolute()]
        args.extend(self.args)

        proc = subprocess.run(
            args=args,
            capture_output=True,
            encoding='utf-8',
            text=True,
            shell=shell,
            timeout=self.timeout,
        )

        return proc

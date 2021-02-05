import pathlib
import platform
import subprocess

from typing import List

from . import Printer


class PrintTool:
    """Generic PrintTool"""

    def __init__(self, name: str, printer: Printer, app_path: pathlib.Path, args: List[str]):
        self.name = name
        self.printer = printer
        self.app_path = app_path
        self.args = args

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

    def run(self, timeout=30) -> subprocess.CompletedProcess:
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
            timeout=timeout,
        )
        return proc

    # def print_file(self, file: pathlib.Path, args_placeholder: str = None) -> bool:
    #     proc = self.run()
    #     print(proc)
    #     print(proc.returncode)
    #
    #     if proc.returncode == 0:
    #         return True
    #     return False

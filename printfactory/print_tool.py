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

    def exists(self) -> bool:
        return self.app_path.exists()

    def get_args(self) -> List[str]:
        return self.args

    def set_args(self, args: List[str]) -> List[str]:
        self.args = args
        return self.args

    def add_args(self, args: List[str]) -> List[str]:
        self.args.extend(args)
        return self.args

    def print_file(self, file: pathlib.Path) -> bool:
        args = None
        shell = False
        pltfrm = platform.system()
        if pltfrm == 'Windows':
            args = [self.args, file]
        # elif pltfrm == 'Darwin':
        #     args = []
        #     shell = True
        else:
            raise NotImplementedError

        print('\n')
        print('#'*100)
        print(f'args = {args}')
        print('#'*100)

        proc = subprocess.run(
            args=self.args,
            capture_output=True,
            encoding='utf-8',
            text=True,
            shell=shell,
        )

        print(proc)
        print(proc.returncode)
        print('#'*100)

        if proc.returncode == 0:
            return True
        return False

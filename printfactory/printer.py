import pathlib
import platform
import subprocess

from typing import List


class Printer:
    """Main printer class"""

    def __init__(
            self,
            printer_name: str = None,
            driver_name: str = None,
            port_name: str = None,
    ):
        """
        Initialize Printer class

        :param printer_name: Name of the printer, use systems default printer if not given
        :param driver_name: Driver name that should be used
        :param port_name: Port of the printer
        """
        self.name: str = printer_name
        self.driver: str = driver_name
        self.port: str = port_name

    @staticmethod
    def get_list() -> list:
        """Get a list of installed printers

        :return: List of printers
        """
        # @todo: Return default system printer name at position 0
        args = None
        shell = False
        pltfrm = platform.system()
        if pltfrm == 'Windows':
            args = ['wmic', 'printer', 'get', 'name']
        elif pltfrm == 'Darwin':
            args = ["lpstat -p | awk '{print $2}'"]
            shell = True

        proc = subprocess.run(
            args=args,
            capture_output=True,
            encoding='utf-8',
            text=True,
            shell=shell,
        )

        lines = proc.stdout.splitlines()
        printers = []

        for line in lines:
            line = line.strip()
            if line not in ['', 'Name', '\n']:
                printers.append(line)

        return printers


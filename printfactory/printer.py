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
            _default: bool = False
    ):
        """
        Initialize Printer class

        :param printer_name: Name of the printer, use systems default printer if not given
        :param driver_name: Driver name that should be used
        :param port_name: Port of the printer
        :param _default: True if printer is the systems default printer, else False
        """
        self.name: str = printer_name
        self.driver: str = driver_name
        self.port: str = port_name
        self._default: bool = _default

    @staticmethod
    def get_list() -> List['Printer']:
        """Get a list of installed printers

        :return: List of printers
        """
        # @todo: Return default system printer name at position 0
        args = None
        shell = False
        pltfrm = platform.system()
        if pltfrm == 'Windows':
            # args = ['wmic', 'printer', 'get', 'Name']
            args = ['wmic', 'printer', 'get', 'Default,DriverName,Name,PortName']
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

        print('\n')
        print('#'*100)
        for line in lines:
            line = line.strip()
            if line not in ['', 'Name', '\n']:
                print(line)
                printers.append(line)
        print('#'*100)

        return printers

    @classmethod
    def get_default(cls) -> 'Printer':
        """Get the default printer

        :return: Printer
        """
        args = None
        shell = False
        pltfrm = platform.system()
        if pltfrm == 'Windows':
            args = ['wmic', 'printer', 'get', 'Default', 'DriverName', 'Name', 'PortName']
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




        return cls(
            printer_name=None,
            driver_name=None,
            port_name=None,
        )

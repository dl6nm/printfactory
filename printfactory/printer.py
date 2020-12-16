import pathlib
import platform
import subprocess

from enum import Enum


def list_printers() -> list:
    """Get a list of installed printers

    :return: List of printers
    """
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


class PrintToolEnum(str, Enum):
    ADOBE_ACROBAT = 'Adobe Acrobat'
    ADOBE_READER = 'Adobe Reader'
    FOXIT_READER = 'Foxit Reader'


class PrintTool:
    name: PrintToolEnum
    path: pathlib.Path


class Printer:
    """
    Main printer class

        - initialize Printer class
        - set printer options
        - auto-check
            - available pdf reader (Acrobat, Adobe Reader, Foxit Reader, ...)
            - available printers (get list)
        - print document
    """

    def __init__(
            self,
            name: str = None,
            driver: str = None,
            port: str = None,
            print_tool: PrintTool = None,
    ):
        """
        Base printfactory class

        :param name: Name of the printer, use systems default printer if not given
        :param driver: Driver name that should be used
        :param port: Port of the printer
        :param print_tool: Platform dependent tool, used for printing a file
        """
        self.name: str = name
        self.driver: str = driver
        self.port: str = port
        self.print_tool = print_tool

        pltfrm = platform.system()
        if print_tool is None:
            if pltfrm == 'Windows':
                self.print_tool = PrintToolEnum.ADOBE_READER
            elif pltfrm == 'Darwin':
                raise NotImplementedError
            else:
                raise NotImplementedError

    def print_file(self, filename):
        if self.middleware in ['AdobeReader', 'AdobeAcrobat']:
            # if windows
            subprocess.run(['AcroRd32.exe', '/t', 'my.pdf', self.name, self.driver, self.port])
        return True


class AcroPrinter(Printer):
    """
    Adobe Acrobat DC and Adobe Reader specific printer class

    !!! Windows only !!!

    Using Adobe Reader (AcroRd32.exe) or Adobe Acrobat (Acrobat.exe)

    AcroRd32.exe [OPTIONS] PATHNAME
        /n  Start a separate instance of Acrobat or Adobe Reader, even if one is currently open.
        /s  Suppress the splash screen.
        /o  Suppress the open file dialog box.
        /h  Start Acrobat or Adobe Reader in a minimized window.
        /p  Start Adobe Reader and display the Print dialog box.

    AcroRd32.exe /t PATH [PRINTERNAME] [DRIVERNAME] [PORTNAME]
        Start Adobe Reader and print a file while suppressing the Print dialog box. The PATH must be fully specified.
        PRINTERNAME     The name of your printer. If not specified, the systems default printer is used.
        DRIVERNAME      Your printer driver’s name, as it appears in your printer’s properties.
        PORTNAME        The printer’s port. PORTNAME cannot contain any "/" characters;
                        if it does, output is routed to the default port for that printer.
    """
    path = {
        # default path: Program Files\Adobe\<product name and version>
    }
    options = {}


class FoxitPrinter(Printer):
    """
    Foxit Reader specific printer class
    """
    options = {}


class LPRPrinter(Printer):
    """
    macOS LPR printer class

    lpr [options] file(s)
        -H server[:port]
             Specify an alternate server.
        -P destination[/instance]
             Print files to the named printer.
        -# copies
             Sets the number of copies to print.
    """
    options = {}


if __name__ == '__main__':
    print(f'printers = {list_printers()}')

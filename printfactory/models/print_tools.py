import os
import pathlib

from pydantic import BaseModel


class AdobeReader(BaseModel):
    """
    Adobe Reader specific model

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
    name: str = 'Adobe Reader'
    _programfiles: str = os.getenv('PROGRAMFILES(X86)')
    app_path: pathlib.Path = pathlib.Path(f'{_programfiles}/Adobe/Acrobat Reader DC/Reader/AcroRd32.exe')

    printer: str = None
    driver: str = None
    port: str = None

    def __init__(self, printer=None, driver=None, port=None) -> None:
        super().__init__(printer=printer, driver=driver, port=port)
        self.printer: str = printer
        self.driver: str = driver
        self.port: str = port

    def get_args(self, print_file: pathlib.Path) -> list:
        args = [
            self.app_path,
            '/t',
            print_file.absolute(),
            self.printer,
            self.driver,
            self.port,
        ]

        if not self.printer and self.driver:
            raise TypeError('Missing printer')
        elif not self.driver and self.port:
            raise TypeError('Missing driver')

        return list(filter(None, args))


# class AcroPrinter(BaseModel):
#     """
#     Adobe Acrobat DC and Adobe Reader specific printer class
#
#     !!! Windows only !!!
#
#     Using Adobe Reader (AcroRd32.exe) or Adobe Acrobat (Acrobat.exe)
#
#     AcroRd32.exe [OPTIONS] PATHNAME
#         /n  Start a separate instance of Acrobat or Adobe Reader, even if one is currently open.
#         /s  Suppress the splash screen.
#         /o  Suppress the open file dialog box.
#         /h  Start Acrobat or Adobe Reader in a minimized window.
#         /p  Start Adobe Reader and display the Print dialog box.
#
#     AcroRd32.exe /t PATH [PRINTERNAME] [DRIVERNAME] [PORTNAME]
#         Start Adobe Reader and print a file while suppressing the Print dialog box. The PATH must be fully specified.
#         PRINTERNAME     The name of your printer. If not specified, the systems default printer is used.
#         DRIVERNAME      Your printer driver’s name, as it appears in your printer’s properties.
#         PORTNAME        The printer’s port. PORTNAME cannot contain any "/" characters;
#                         if it does, output is routed to the default port for that printer.
#     """
#     pass
#
#
# class FoxitPrinter(BaseModel):
#     """
#     Foxit Reader specific printer class
#     """
#
#
# class LPRPrinter(BaseModel):
#     """
#     macOS LPR printer class
#
#     lpr [options] file(s)
#         -H server[:port]
#              Specify an alternate server.
#         -P destination[/instance]
#              Print files to the named printer.
#         -# copies
#              Sets the number of copies to print.
#     """
#     pass

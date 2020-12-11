class Printer:
    """
    Main printer class

        - initialize Printer class
        - set printer options
        - auto-check
            - available pdf reader (Acrobat, Adobe Reader, Foxit Reader
            - available printers (get list)
    """

    def __init__(self, printer: str, driver: str = None, port: str = None):
        pass


class AcroPrinter(Printer):
    """
    Adobe Acrobat DC and Adobe Reader specific printer class

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
    options = {}


class FoxitPrinter(Printer):
    """
    Foxit Reader specific printer class
    """
    options = {}


class LprPrinter(Printer):
    """
    macOS LPR printer class
    """
    options = {}


class PrintFactory:
    """


        - initialize printer
        - print document
    """
    pass


if __name__ == '__main__':
    from sys import version
    print(version)

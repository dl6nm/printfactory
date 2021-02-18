# `printfactory` notes and ideas

## structure

    printfactory
        .list_printers()        # list/get available printers in system

        Printer()               # Generic Printer class for printing a file with a PrintTool
            .send()             # send a file to a printer using a PrintTool

        AcroPrinter(Printer)    # Subclass of Printer() for Adobe Acrobat
        AcroRdPrinter(Printer)  # Subclass of AcroPrinter() for Adobe Reader
       [FoxitPrinter(Printer)]  # Subclass of Printer() for Foxit Reader
       [LPRPrinter(Printer)]    # Subclass of Printer() for LPR printing on Linux like systems

        PrintTools()            # List/Enum of implemented tools for printing a file
            .find()             # Find a PrintTool in system
            .available()        # List available PrintTools on a system

        PrintTool()             # List/Enum of implemented tools for printing a file
            Adobe Acrobat
            Adobe Reader
            Foxit Reader
            LPR

    printer = printfactory.Printer('PrinterName')   # return Printer class
    printer.tool => AdobeReader                     # autodetect path
    printed = printer.send('PathToPDFDocument')     # return True or False

# printfactory

`printfactory` is a package, primarily for printing PDF files to a physical printer.

[comment]: <> ([![Badges @ Shields IO][shield-badges]][shields])
[comment]: <> ([![Version?][shield-version]][shields])
[comment]: <> ([![Build passed?][shield-build]][shields])
[comment]: <> ([![Language?][shield-markdown]][shields])
[![License?][shield-license]](LICENSE)

## Table of Contents

- [Why?](#why)
- [Changelog](#changelog)

## Why?

The motivation for this project was to have a simple Python interface for printing PDF files to a physical printer.
Only public available and free software should be used on the client or server using this package. 


## printfactory package

    printfactory
        .list_printers()     # list/get available printers in system
                                Windows CMD: wmic printer get name
                                macOS: lpstat -p | awk '{print $2}'

        Printer()           # Generic Printer class for printing a file with a PrintTool
            .send()             # send a file to a printer using a PrintTool

        PrintTools()        # List/Enum of implemented tools for printing a file
            .find()         # Find a PrintTool in system

        PrintTool()         # List/Enum of implemented tools for printing a file
            Adobe Acrobat
            Adobe Reader
            Foxit Reader
            LPR


    printer = printfactory.Printer('PrinterName')   # return Printer class
    printer.tool => AdobeReader                     # autodetect path
    printed = printer.send('PathToPDFDocument')     # return True or False



## Changelog

All notable changes to this project will be documented in the [CHANGELOG.md](CHANGELOG.md).



[shield-license]:  https://img.shields.io/badge/license-MIT-blue.svg

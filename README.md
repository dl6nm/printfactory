# printfactory

`printfactory` is a package for printing PDF files to a physical printer 
using a print tool like [Adobe Reader][AdobeReader] or [Foxit Reader][FoxitReader].

[![License?][shield-license]](LICENSE)

**Example usage**

    import pathlib
    import printfactory

    printer = printfactory.Printer(
        printer_name='My Printers Name',
    )

    print_file = pathlib.Path('path/to/my.pdf')
    printer.send(print_file)

## Table of Contents

- [Why?](#why)
- [Requirements](#requirements)
- [Installing `printfactory`](#installing-printfactory)
- [Changelog](#changelog)

## Why?

The motivation for this project was to have a simple Python interface
for printing PDF files to a physical printer using a local installed software _("print-tool")_.

Only publicly and freely available software should be used on the client or server that is using this package.

## Requirements

- [Python >= 3.8][python]
- [pip][pip]

## Installing `printfactory`

To install the latest version of `printfactory` use pip as simple as follows.

    pip install printfactory

## Contributing

If you'd like to contribute to this project [Poetry][poetry] is recommended.

## Changelog

All notable changes to this project will be documented in the [CHANGELOG.md](CHANGELOG.md).



[shield-license]: https://img.shields.io/badge/license-MIT-blue.svg

[AdobeReader]: https://get.adobe.com/reader/
[FoxitReader]: https://www.foxitsoftware.com/pdf-reader/

[python]: https://www.python.org/
[pip]: https://pypi.org/project/pip/
[poetry]: https://python-poetry.org/

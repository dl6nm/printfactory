# printfactory Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

## [Unreleased]

### [0.1.0] (2020-02-10)

#### Added

- add basic app skeleton example with tests and docs
- add _Printer_ class to set up a printer for a PrintTool
- add a function to get a list of installed printers on your system 
- add generic _PrintTool_ class for sending files to a printer
- add _AdobeReader_ class for sending files to a _Printer_
- add _AdobeAcrobat_ class for sending files to a _Printer_

#### Known issues

- The _AdobeAcrobat_ print tool implementation is limited to only send files to the defaults system printer  

## [Releases]

No releases yet...


[unreleased]: https://github.com/dl6nm/printfactory/compare/master...develop
[0.1.0]: https://github.com/dl6nm/printfactory/releases/tag/0.1.0

[releases]: https://github.com/dl6nm/printfactory/releases

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html

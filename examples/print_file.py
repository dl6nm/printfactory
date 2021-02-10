import pathlib
import printfactory

# Initializing Printer and PrintTool
printer = printfactory.Printer()
print_tool = printfactory.AdobeReader(printer)

# Printing a PDF file
file = pathlib.Path('my.pdf')
print_tool.print_file(file)

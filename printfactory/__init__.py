from importlib.metadata import version

__version__ = version('printfactory')


from .printer import *
from .print_tool import *

__all__ = [
    'Printer',
    'PrintTool',
]

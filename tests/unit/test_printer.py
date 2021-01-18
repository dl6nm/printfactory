import pytest

from printfactory.printer import Printer


@pytest.mark.parametrize(
    argnames='print_file_name',
    argvalues=['my.pdf'],
)
class TestPrinterDefaults:
    """Test default Printer"""

    printer = Printer()

    def test_default_attributes(self):
        assert self.printer.name == 'BlackHole'
        assert self.printer.driver is None
        assert self.printer.port is None

    def test_get_list(self):
        # instance method
        assert 'BlackHole' in Printer.get_list()
        # static method
        assert 'BlackHole' in self.printer.get_list()

    def test_get_default(self):
        # instance method
        assert 'BlackHole' in self.printer.get_default()
        # static method
        assert 'BlackHole' in Printer.get_default()

    def test_send_file(self, shared_datadir, print_file_name):
        print_file = shared_datadir / print_file_name
        assert self.printer.send_file(print_file=print_file) is None

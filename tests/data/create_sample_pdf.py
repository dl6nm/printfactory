"""Create a DIN A4 pdf file with a number in the middle of the page"""
from reportlab.pdfgen.canvas import Canvas

PAGESIZE_PT = (595.276, 841.89)

canavs = Canvas('my.pdf')
canavs.setPageSize(PAGESIZE_PT)
canavs.drawString(PAGESIZE_PT[0]/2, PAGESIZE_PT[1]/2, '1')
canavs.save()

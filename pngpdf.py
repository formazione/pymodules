from fpdf import FPDF
from PIL import Image


def makePdf(pdfFileName, listPages, dir=''):
    "Takes filename and number of pages abd creates pdf"
    if (dir):
        dir += "/"

    cover = Image.open(dir + str(listPages[0]))
    width, height = cover.size

    pdf = FPDF(unit="pt", format=[width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page), 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")


import os.path
x = [f for f in os.listdir() if f.endswith(".png")]
print(x)
y = len(x)


nomefile = input("Nomedelfile: ")

makePdf(nomefile, x)

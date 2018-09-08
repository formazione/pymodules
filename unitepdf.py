import PyPDF2
import os

print("This program will unite all the pdf in this folder")
print("Insert the name of the pdf you want to make:")
name = input("Name: ")
if name.endswith(".pdf"):
    pass
else:
    name = name + ".pdf"
# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
# put them into an ordered list
pdfFiles.sort()
# I create the istance to create the pdf
pdfWriter = PyPDF2.PdfFileWriter()
# Loop through all the PDF files.
for filename in pdfFiles:
    # Apre ogni pdf
    pdfFileObj = open(filename, 'rb')
    # Ne legge oò contenuto
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Mette ogni pagina nell'oggetto di scrittura
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
# Salva e chiude il file "Complete.pdf"
pdfOutput = open(name, 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

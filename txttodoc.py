# file per convertire un file txt in docx

from docx import Document
import glob
import os

doc = Document()

for txt in glob.glob("*txt"):
    print(txt)

input_txt = input("file da convertire in docx: ")
if input_txt.endswith(".txt"):
    pass
else:
    input_txt += ".txt"

with open(input_txt, 'r', encoding='utf-8') as file:
    doc.add_paragraph(file.read())

input_doc = input("Nome del file da salvare come docx: ")
if input_doc.endswith(".docx"):
    pass
else:
    input_doc += ".docx"

doc.save(input_doc)
os.system("start " + input_doc)

# -*- encoding: utf-8 -*-
import os

# this is the start of the code


def head():
    "This goes into the head"
    return """</html>
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://formazione.github.io/css/ext.css">
    <style>
    .blue {
    color : blue;
    }

    h2 {
    color: darkgray;
    }




    </style>
    </head>"""


class Div:
    collector = {}  # this collect all the istances of the class

    def __init__(self, title, paragraph="", img=""):
        self.title = title
        self.paragraph = paragraph
        self.img = img
        self.button = ""
        self.divcontent()
        Div.collector[self.title] = self

    def divcontent(self):
        "Each section is made with this code"
        # Here is the title of the section, the paragraph and buttons
        return """<div class="container">
        <h2>""" + self.title + """</h2>
            <p>""" + self.paragraph + """</p>""" \
            + self.button + """</div>"""

    def add_paragraph(self, content):
        self.paragraph += "<p>" + content + "</p>"

    def add_list(self, lista):
        "* after the : and # after ,"
        '''  === Istruzioni per aggiungere un elenco puntato ===
    per creare una lista, inserisci un asterisco dopo i due punti
    e un # dopo ogni virgola o punto e virgola di ogni item
        '''
        lista = lista.split("*")
        self.paragraph += "<b class='blue'>" + lista[0] + "</b><ul>"
        for items in lista[1].split("#"):
            # Visualizza ciò che è tra parentesi non in bold e in italic
            if "(" in items:
                items = items.replace("(", "</b>(<i>").replace(")", "</i>)</b>")
            self.paragraph += "<li><b>" + items + "</b></li>"
        self.paragraph += "</ul></p>"

    def add_image(self, img):
        self.paragraph += """<center><img src=\"""" + img + """"\" / ></center>"""

    def add_button(self, caption):
        self.buttonbody(self.buttonround(caption))

    def buttonround(self, caption):
        return("""<button type="button" class="btn btn-success">""" + caption + """</button> """)

    def buttonquare(self):
        return("""<button type="button" class="btn btn-default">Rounded corners</button>""")

    def buttonbody(self, newbutton):
        "This is the collection of elements into the body"
        self.button += newbutton
        return self.button

# the final part of the code


def end():
    return "\n</html>"


# this showe at console the code
def print_at_console():
    testo = head()
    for k, v in Div.collector.items():
        testo += v.divcontent()
    testo += end()
    print(testo)
# ===== FINE =====

# This saves the file in every self.paragraph into htmlfile


def create_html_file(htmlfile, see=0):
    with open(htmlfile, 'w', encoding='utf-8') as file:
        testo = head()
        for k, v in Div.collector.items():
            testo += v.divcontent()
        testo += end()
        file.write(testo)
    if see == 1:
        os.system(htmlfile)
    return htmlfile


class Extern:
    def __init__(self, _file):
        with open(_file, 'r', encoding='utf-8') as file:
            l = Div(file.readline())
            for line in file.readlines():
                l.add_paragraph(line)

# here I add the content


class Paragraph:
    "Crea un oggetto Div e aggiunge i parametri per add_paragraph e add_list ecc."

    def __init__(self, title, paragraph, lista='', img='', end=''):
        self.div0 = Div(title)
        self.div0.add_paragraph(paragraph)
        if lista != "":
            self.div0.add_list(lista)
        if img != '':
            self.div0.add_image(img)
        if end != '':
            self.div0.add_paragraph(end)


"""
Put here all your paragraph
if you want to make more book create another Book class
"""
print("Read all the txt file and make an html out of them")
what_to_see = input("Cosa vuoi vedere (invio se vuoi vedere tutto): ")
for file in os.listdir():
    if ".txt" in file:
        if what_to_see in file:
            Extern(file)


create_html_file("file.html", see=1)  # This write the file
# listaparagrafi1[0][0] è il primo titolo, unito con _ per permettere a os.system di aprirlo

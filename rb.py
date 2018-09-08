import glob
import os
import re
'''
Creazione di domande a risposta breve
- legge tutti i file di testo presenti nella cartella
- crea il codice da incollare in wp
- si crea uno shortcode
- lo si mette nella pagina

Si basa su un altro shortcode = input 2
Questo crea i radio buttons e l'eventlistener

Le domande nel file di testo:

Con il contratto di __________ una parte trasferisce all'altra la proprietà di un bene dietro pagamento di un prezzo (art. 1470 c.c.) / compravendita

'''

start = """[hoops name="guessWhat"]<script>\n"""
print(start)
num = 0
for file in glob.glob("*.html"):
    num += 1
    content = ""
    with open(file, "r", encoding="utf-8") as file:
        for line in file:
            dom = line.split("--")
            dom_start = dom[0]
            giusta = dom[1]
            dom_end = dom[2]
            if dom[0][0] == "#":
                tipodirisposta = "guessWhat"
                dom[0] = dom[0].replace("#", "")
            else:
                tipodirisposta = "input"
            content += tipodirisposta + "(\"" + dom_start + "\", \"" + giusta.strip() + "\",\"" + dom_end.strip() + "\");\n"
            file.readline()

    end = """addsol();</script>"""

    print(content)

    end = "</script>"


def txtfile():
    with open("file" + str(num) + ".htm", "w", encoding="utf-8") as file:
        file.write(start + content + end)
    #os.system("file" + str(num) + ".htm")


def _tobeprinted():
    global listofk
    with open("file" + str(num) + "_print.htm", "w", encoding="utf-8") as file:
        with open(glob.glob("*.html")[0], "r", encoding='utf-8') as filehtml:
            f = filehtml.read()
            listofk = re.findall("--(.*)--", f)
            f = f.replace("--", "").replace("*", "")
            for k in listofk:
                f = f.replace(k, "_____________")
            file.write(f)
            print("questo è filehtml-------------")
            print(filehtml)
    os.system("file" + str(num) + "_print.htm")


print(end)
txtfile()
_tobeprinted()

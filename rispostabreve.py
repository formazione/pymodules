import glob

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

num = 0
for file in glob.glob("*.txt"):
    num += 1
    start = """[hoops name="input2"]
    <script>\n"""
    content = ""
    with open(file, "r", encoding="utf-8") as file:
        for line in file:
            content += "input(\"" + line.split("/")[0] + "\", \"" + line.split("/")[1].strip() + "\");\n"
            file.readline()

    end = """</script>"""

    print(start + content + end)

    with open("file" + str(num) + ".html", "w", encoding="utf-8") as file:
        file.write(start + content + end)

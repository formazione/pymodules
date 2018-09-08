# REGOLE sub6_2_jumpGUI.py --------- ESEMPIO ----------
'''
OUbqytVF-F0
nella riga 1 se scrivo x12x00 comincia al minuto 12, se non inizia per x ignora la riga e comincia da 0:0
03 traduzione di Giovanni Gatto
11 ci avete chiesto spesso cosa usa Abigail per comunicare
16 a causa della mancanza di alcune abilità motorie e per renderglielo più semplice
x3x00 salta al minuto 3
19 il linguaggio dei segni è leggermente modificato
20 per andare incontro a questo
22 ok, sei pronta?
24 sì, sei pronta?
# --------------- questo è un commento---------------------------
'''

import tkinter as tk


def createSub(aotv, tots):
    'creates the subtitles in the way that the js script accepts'
    indirizzo_video = aotv          # Address Of The Video
    sub_txt = tots                  # Text Of The Subtitles
    subtitle = 'subtitle' + sub_txt  # this makes the subtitle unique in the web page in case of more videos
    video = "video" + sub_txt       # this make a unique referrement to the video
    sub_txt = sub_txt + ".txt"      # adding .txt to the name of the file of the subtitles
    sub_js = "sub_" + sub_txt + ".js"  # not used; I must implement the choice to choose the type of subtitles

    # ========================== codice_wp lista del codice html da visualizzare ==========
    codice_wp = []
    codice_wp.append("<iframe id=\"" + video + "\" width=\"100%\" height=\"500\" src=\"https://www.youtube.com/embed/" + indirizzo_video + "\" frameborder=\"0\" allowfullscreen></iframe>")
    codice_wp.append("""
    <!-- subtit_em.js subtut_1m.js subtit_2m.js (non funziona?) sub16em.js -->
        """)
    codice_wp.append("<script src=\"https://sportelloautismo.github.io/js/sub16em.js\"></script>")
    codice_wp.append("<script>\nvar " + subtitle + " = [")

    with open(sub_txt, encoding="utf-8") as file:
        testo = file.readlines()
        for line in range(len(testo)):
            if line == 0:
                continue
            elif line == 1:
                # Alla prima linea ci può essere l'indicazione di partire da un tempo
                # diverso da x0x0, ad esempio 10x12
                # altrimenti, se non c'è x si parte da 0
                if testo[line][:1] == "x":
                    jump = testo[line].split("x")
                    min = int(jump[1])
                    sec = int(jump[2])
                # Se non c'è la x nella prima riga, si inizia da zero
                else:
                    min = 0
                    sec = 0
                continue
            # Quando siamo oltre la prima linea, se si incontra una x si salta al temp x5x30 ad esempio
            elif testo[line][:1] == "x":
                jump = testo[line].split("x")
                min = int(jump[1])
                sec = int(jump[2])
                continue
            elif testo[line][:1] == "#":
                # this is used to write the time or other stuff the program ignore
                continue
            s1 = min * 60 + sec
            sec2 = int(testo[line][:2])
            if sec2 < sec:
                min += 1
            e1 = min * 60 + sec2
            text = testo[line].rstrip("\n")
            # text = text.replace("\"","\'")
            codice_wp.append("{\"start\": " + str(s1) + ".1,")
            codice_wp.append("\"end\" :" + str(e1) + '.0,')
            text = text.replace("\"", "'")
            codice_wp.append("\"text\" :\"" + text[3:] + "\"},")
            sec = sec2


    codice_wp.append("];\nvar youtubeExternalSubtitle = new YoutubeExternalSubtitle.Subtitle(document.getElementById('" + video + "'), " + subtitle + ");\n</script>")

    for code in codice_wp:
        print(code)
# INTERFACCIA GRAFICA


root = tk.Tk()
root.title("Subtitle Maker")
root.geometry("250x150")
root.configure(bg='green')
var = tk.StringVar()
label = tk.Message(root, textvariable=var, relief=tk.RAISED, bg='yellow')
var.set("insert file and press enter")
label.pack()

# LEGGE IL NOME DEL VIDEO NEL FILE


def start():
    with open(vartesto.get() + ".txt") as file:
        a = file.readline().strip()
    varvideo.set(a)
    createSub(varvideo.get(), vartesto.get())


varvideo = tk.StringVar()
entryvid = tk.Entry(root, textvariable=varvideo, bg='pink')
entryvid.pack()

vartesto = tk.StringVar()
entry = tk.Entry(root, textvariable=vartesto, bg='lightblue', bd=4)
entry.pack()
entry.focus_set()

text = tk.Text(root)
text.pack()

root.bind("<Return>", lambda x: start())
root.mainloop()

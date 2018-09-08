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


def createSub(tots):
    'creates the subtitles in the way that the js script accepts'
    sub_txt = tots                  # Text Of The Subtitles
    subtitle = 'subtitle' + sub_txt  # this makes the subtitle unique in the web page in case of more videos
    video = "video" + sub_txt       # this make a unique referrement to the video
    sub_txt = sub_txt + ".txt"      # adding .txt to the name of the file of the subtitles
    with open(sub_txt) as file:
        aotv = file.readline().strip().split("/")[3]
    indirizzo_video = aotv          # Address Of The Video
    # sub_js = "sub_" + sub_txt + ".js"  # not used; I must implement the choice to choose the type of subtitles

    print("<iframe id=\"" + video + "\" width=\"100%\" height=\"500\" src=\"https://www.youtube.com/embed/" + indirizzo_video + "\" frameborder=\"0\" allowfullscreen></iframe>")
    print("""
    <!-- subtit_em.js subtut_1m.js subtit_2m.js (non funziona?) sub16em.js -->
        """)
    print("<script src=\"https://sportelloautismo.github.io/js/sub16em.js\"></script>")
    print("<script>\nvar " + subtitle + " = [")
    txtinsert1 = "<iframe id=\"" + video + "\" width=\"100%\" height=\"500\" src=\"https://www.youtube.com/embed/" + indirizzo_video + "\" frameborder=\"0\" allowfullscreen></iframe>" + \
        "<script src=\"https://sportelloautismo.github.io/js/subBigDark.js\"></script>" +\
        "<script>\n\nvar " + subtitle + " = ["

    txtinsert2 = ''
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
            print("{\"start\": " + str(s1) + ".1,")
            print("\"end\" :" + str(e1) + '.0,')
            text = text.replace("\"", "'")
            print("\"text\" :\"" + text[3:] + "\"},")
            # THIS GOES INTO THE TXT AREA OF THE GUI SUBTITLES_G8 VERSION
            txtinsert2 += "{\n\"start\": " + str(s1) + ".1," +\
                "\n\"end\" :" + str(e1) + '.0,' +\
                "\n\"text\" :\"" + text[3:] + "\"},\n"

            sec = sec2

    print("];\nvar youtubeExternalSubtitle = new YoutubeExternalSubtitle.Subtitle(document.getElementById('" + video + "'), " + subtitle + ");\n</script>")
    txtinsert3 = "];\n\nvar youtubeExternalSubtitle = new YoutubeExternalSubtitle.Subtitle(document.getElementById('" + video + "'), " + subtitle + ");\n</script>"
    txtgui.insert(0.0, txtinsert1 + txtinsert2 + txtinsert3)

# INTERFACCIA GRAFICA


root = tk.Tk()
root.title("Subtitle Maker")
root.geometry("450x550")
root.configure(bg='green')
var = tk.StringVar()
label = tk.Message(root, textvariable=var, relief=tk.RAISED, bg='yellow')
var.set("inserisci il nome del file con i sottotitoli e premi enter")
label.pack()

vartesto = tk.StringVar()
entry = tk.Entry(root, textvariable=vartesto, bg='lightblue', bd=4)
entry.pack()
entry.focus_set()

txtgui = tk.Text(root, wrap=tk.WORD)
txtgui.pack(fill=tk.BOTH, expand=1)

# Quando premi enter va a createSub
root.bind("<Return>", lambda x: createSub(vartesto.get()))
root.mainloop()

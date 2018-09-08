from gtts import gTTS


def introduzione():
    "Introduzione al programma con alcune istruzioni"
    print("Un programma di Giovanni Gatto - 15/01/2018")
    print("Inserisci il testo nella variabile testo")
    print("Avvia il programma e inserisci il nome del file mp3 senza l'estensione del tipo di file.")
    print("--------------- have fun! ----------")
    print()


def start():
    "Chiede il nome del file, lo crea, lo salva, lo esegue"
    global testo
    introduzione()
    name = input("Nome del file (con .mp3): ")
    try:
        tts = gTTS(testo, 'it')
        tts.save(name)

        print("Il file è stato salvato, ora verrà avviato il programma del computer per ascoltarlo.")
        print("... wait")
        print()
        import os
        os.system("start " + name + ".mp3")
    except:
        print("...")
        print("Attenzione:")
        print("\til programma non funziona senza connessione a Internet.")



# Inserisci il testo qui
testo = """
Testo di esempio da trasformare in mp3
"""
# testo = getFileFromText(file)
start()

elenco = """
TUTTI I MIEI PROGRAMMI

alldoctopdf_____tutti i doc diventano pdf (usa pdfmerger)

alltxttodoc_____converte tutti i file di testo nella dir in doc

gif_____________crea gif da tutti png nella dir

mp3fromfile_____trasforma un file di testo in audio

pdfmerger_______tutti i pdf uniti in uno

pngpdf__________tutti i png in un file pdf
pngpdf2_________tutti i PNG in un file pdf
                simili:
                    - jpgpdf
                    - gif

presentazioni___da testo a pptx


seefiles________shows the txt files in a dir
                import seefiles
                seefiles.seefiles()

squareimg______makes an colored square image with magick

txttodoc________trasforma testo di un txt in doc

rename__________puts a "0" after Diapositiva
                to ensure that gif works with
                powerpoint saved to png
                code:
                    import rename
                    rename.rename()
searching       python searching.py andrea
                trova il file in cui c'è scritto andrea
"""


print(*(e for e in elenco.splitlines()), sep="\n")

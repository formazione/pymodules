import os

if os.path.isfile("00.PNG"):
    for f in os.listdir():
        if ".PNG" in f:
            os.remove(f)


def rename():
    x = [a for a in os.listdir() if 'PNG' in a]
    for n, name in enumerate(x):
        if name.startswith("Diapositiva0"):
            os.rename(name, "Diapositiva" + str(n) + ".PNG")
        else:
            os.rename(name, "Diapositiva0" + str(n) + ".PNG")


rename()
import gif

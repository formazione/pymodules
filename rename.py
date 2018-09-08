import os


def rename():
    x = [a for a in os.listdir() if 'PNG' in a]

    for f in x:
        if "0" in f:
            os.rename(f, f[:11] + "0" + f[11:])
        else:
            os.rename(f, f[:11] + "00" + f[11:])

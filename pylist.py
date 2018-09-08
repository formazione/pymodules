# pylist


def help():
    for f in dir(pylist):
        print(f)


def listFromString(stringa):
    "Returns a list with a item = each line from a multilines string"
    stringa = stringa.split("\n")
    if stringa[0] == '':
        stringa.pop(0)
    if stringa[-1] == '':
        stringa.pop(-1)
    return stringa


def listFromTxt(txt):
    "returns a list from lines in a txt file"
    t = []
    with open(txt, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

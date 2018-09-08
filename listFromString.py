def listFromString(stringa):
    stringa = stringa.split("\n")
    if stringa[0] == '':
        stringa.pop(0)
    if stringa[-1] == '':
        stringa.pop(-1)
    return stringa

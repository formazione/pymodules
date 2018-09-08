import os
import re


def rename():
    x = [a for a in os.listdir() if 'PNG' in a]
    for f in x:
        num = re.search("[0-9]+", f)
        num1 = "0" + num
        newname = re.sub(num, num1)
        os.rename(newname)

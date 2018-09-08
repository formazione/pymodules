import re
from random import randint, shuffle
import glob
import os


class ShakeData:
    def __init__(self, text):
        pass
        self.text = text
        with open(self.text, 'r') as file:
            self.data = file.read().splitlines()
        for n, d in enumerate(self.data):
            rnd = str(randint(1, 50) * 100)
            self.data[n] = re.sub("[0-9]+", rnd, d)
        self.printshuffle()

    def printshuffle(self):
        shuffle(self.data)
        self.content = []
        for f in self.data:
            f = f.split()
            line = "{:20}{:3}{:3}".format(*f)
            print(line)
            self.content.append(line)
        print("\n")
        return self.content


file = glob.glob("*.txt")[0]


def helper():
    print("Example of using the shakedata module")
    print("")
    print("from esercizi.shakedata import ShakeData\n")
    print("ShakeData(file)\n")


for n in range(3):
    ShakeData(file)

import os
import sys

searching = ""
try:
    searching = sys.argv[1]
except:
    searching = input("Cosa cerchi? ")

for file in os.listdir():
    if '.txt' in file:
        with open(file) as f:
            if searching in f.read():
                print(file)

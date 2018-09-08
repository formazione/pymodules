import os
inp = input("Cosa cerchi?:> ")
thisdir = os.getcwd()
for r, d, f in os.walk(thisdir):
    for file in f:
        if inp in file:
            print(os.path.join(r, file))

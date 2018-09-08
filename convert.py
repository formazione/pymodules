"""
convert -delay 200 1.gif -coalesce \( -delay 30 2.gif -coalesce \) animated.gif

convert -size 450x300 xc:red f1.gif
convert -size 450x300 xc:red f1.gif
convert -delay 100 f1.gif -delay 30 f2.gif
"""
import os
import re

gif = [(g, re.findall("[0-9]+", g)) for g in os.listdir() if '.gif' in g and re.match("[0-9]+", g)]

stringa = "convert "
for count, img in enumerate(gif):
    stringa += "-delay " + img[1][0] + " " + img[0] + " "

stringa += "new.gif"
print(stringa)
os.system(stringa)

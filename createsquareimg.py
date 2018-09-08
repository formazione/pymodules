import os

__documentation__ = "This program creates a colored square image of the dimension you want"


name = input("name (img) ")
size = input("size (40) ")
size += "x" + size
color = input("color (red) ")
extension = input("extention (gif, jpg or png? ")


def squareimg(name="img", size="40x40", color="red", extension="gif"):
    os.system("magick convert -size " + size + " xc:" + color + " " + name + "." + extension)


squareimg(name, size, color, extension)

import subprocess
import os


def mk(i, o):
    """i=the input file, all of them 0=the gif output file"""
    subprocess.call("convert " + i + " " + o, shell=True)


mk("*.png", "my.jpeg")
print("The jpeg are here")

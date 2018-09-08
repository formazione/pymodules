# seefiles
import os
import glob


print("seetxtfiles()\nseefiles()")


def seetxtfiles():
    return glob.glob("*txt")


def seefiles():
    return os.listdir()

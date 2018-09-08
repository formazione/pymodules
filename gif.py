import subprocess
import os


def mk(i, o, delay=100, loop=5):
    """i=the input file, all of them 0=the gif output file"""
    subprocess.call("convert -delay " +
                    delay + " -loop " + loop + " " + i + " " + o, shell=True)


delay = input("Delay (default 100): ")
loop = input("Loop (default 5): ")
mk("*.png", "output.gif", delay, loop)
os.system("start output.gif")

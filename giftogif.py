import subprocess
import os


def mk(i, o, delay=100):
    subprocess.call("convert -delay " +
                    delay + " -loop 5 " + i + " " + o, shell=True)


delay = input("Delay (default 100): ")
mk("*.gif", "output.gif", delay)
os.system("start output.gif")

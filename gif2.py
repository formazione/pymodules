import subprocess
import os


def mk(i, o, delay=100):
    subprocess.call("convert -delay " +
                    delay + " -loop 5 " + i + " " + o, shell=True)


def mk2(i, o, delay=100):
    subprocess.call("convert -delay " +
                    delay + " -loop 0 " + i + " " + o, shell=True)

print("This makes infinite loop")
delay = input("Delay (default 100): ")
mk2("*.png", "output.gif", delay)
os.system("start output.gif")

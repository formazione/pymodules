from win32com.client import Dispatch
import glob

speak = Dispatch("SAPI.SpVoice")


def readall():
    for f in glob.glob("*txt"):
        filetoread = f
        speak(filetoread)


def speak(filetoread):
    try:
        with open(filetoread, 'r', encoding='utf-8') as file:
            for line in file:
                speak.Speak(line)
    except:
        print("========= ALERT! ===========")
        print("There are no files like that")
        print("========= ALERT! ===========")
        print("P.S.: you have to input the name of a txt file existing in the directory; the files should appear at the start of this window, if there are any.")


dicfile = {}
counter = 1
for eachfile in glob.glob("*txt"):
    key = str(counter)
    dicfile[key] = eachfile
    print(str(counter) + ". " + eachfile)

filetoread = input("Choose the number of file in the list above: ")
# I control that the user puts '.txt' at the end
if ".txt" in filetoread:
    pass
else:
    filetoread = filetoread + ".txt"

speak(filetoread)

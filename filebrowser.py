
import tkinter as tk
import os
from win32com.client import Dispatch


s = Dispatch("SAPI.SpVoice")

# WINDOW CREATION
win = tk.Tk()
geo = win.geometry
geo("400x400+400+400")
win['bg'] = 'orange'

# get the list of files
flist = os.listdir()

lbox = tk.Listbox(win)
lbox.pack()

# THE ITEMS INSERTED WITH A LOOP
for item in flist:
    lbox.insert(tk.END, item)


def showcontent(event, audio=0):
    x = lbox.curselection()[0]
    file = lbox.get(x)
    with open(file, 'r', encoding='utf-8') as file:
        file = file.read()
    text.delete('1.0', tk.END)
    text.insert(tk.END, file)


def audio():
    s.Speak(text.get('1.0', tk.INSERT))


def opensystem(event):
    x = lbox.curselection()[0]
    os.system("start " + lbox.get(x))


button = tk.Button(win, text="audio")
button['command'] = audio
button.pack()

text = tk.Text(win, bg='cyan')
text.pack()
# BINDING OF LISTBOX lbox
lbox.bind("<<ListboxSelect>>", showcontent)
lbox.bind("<Double-Button-1>", opensystem)
# BUTTON

win.mainloop()

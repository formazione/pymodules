''' tk_image_slideshow3.py
create a Tkinter image repeating slide show
tested with Python27/33  by  vegaseat  03dec2013
'''
from itertools import cycle
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
import os


class App(tk.Tk):
    '''Tk window/label adjusts to size of image'''

    def __init__(self, image_files, x, y, delay):
        # the root will be self
        tk.Tk.__init__(self)
        # set x, y position only
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay
        # allows repeat cycling through the pictures
        # store as (img_object, img_name) tuple
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_files)
        self.labels = cycle(x for x in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()
        self.label = tk.Label(text="Ciao", font=(None, 36))
        self.label.pack()
        self.bind("<Right>", lambda x: self.show_slides())

    def show_slides(self):
        '''cycle through the images and show them'''
        # next works with Python26 or higher
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        testo = next(self.labels)
        self.label.config(text=testo)
        # self.label.config(text=lab_text)
        # shows the image filename, but could be expanded
        # to show an associated description of the image
        self.title(img_name)
        #self.label['text'] = next(self.labels)
        # self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()


def helper():
    print("If you see this text you need to:\nPut images in here. Then describe them in labels list.")


try:
    # set milliseconds time between slides
    delay = 3500
    # get a series of gif images you have in the working folder
    # or use full path, or set directory to where the images are
    image_files = [x for x in os.listdir() if '.PNG' in x]
    # Questa lista non viene usata, ora inserisco i nomi dei file sotto le immagini
    labels = ["Questa è la prima immagine",
              "Questa è la seconda",
              "Questa è la terza"]
    # upper left corner coordinates of app window
    x = 100
    y = 100
    app = App(image_files, x, y, delay)
    app.show_slides()
    app.run()
except:
    helper()

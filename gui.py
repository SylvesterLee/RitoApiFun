from tkinter import *
from tkinter.ttk import *

class GUI(object):
    def __init__(self, playersInfo):
        self.win = Tk()
        self.win.title('this is a test window')

        lbl1 = Label(self.win, text = 'label 1')
        lbl2 = Label(self.win, text = 'label 2')
        lbl3 = Label(self.win, text = 'label number 3')
        lbl4 = Label(self.win, text = 'label 4')

        lbl1.grid(column = 0, row = 0, padx = (100,0))
        lbl2.grid(column = 1, row = 0)
        lbl3.grid(column = 0, row = 1, padx = (10,100))
        lbl4.grid(column = 1, row = 1)

        self.win.mainloop()

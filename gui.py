from tkinter import *
from tkinter.ttk import *
import time
class GUI(object):
    def __init__(self, playersInfo):
        self.win = Tk()
        self.win.title('this is a test window')

        for player in playersInfo:
            summonerNameLbl = Label(self.win, text = 'Summoner Name: ' + player['summonerName'])
            championNameLbl = Label(self.win, text = 'Champion Name: ' + player['champName'])
            summonerSpell1NameLbl = Label(self.win, text = 'Summoner Spell 1: ' + player['summonerSpells'][0])
            summonerSpell2NameLbl = Label(self.win, text = 'Summoner Spell 2: ' + player['summonerSpells'][1])





        lbl1 = Label(self.win, text = 'label 1')
        lbl2 = Label(self.win, text = 'label 2')
        lbl3 = Label(self.win, text = 'label number 3')
        lbl4 = Label(self.win, text = 'label 4')

        lbl1.grid(column = 0, row = 0, padx = (100,0))
        lbl2.grid(column = 1, row = 0)

        self.win.mainloop()

        time.sleep(5)

        lbl3.grid(column = 0, row = 1, padx = (10,100))
        lbl4.grid(column = 1, row = 1)

        #self.win.mainloop()

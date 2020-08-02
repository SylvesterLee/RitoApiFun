import RiotConst as Consts
from LiveMatchInfo import LiveMatchInfo
from PlayerInformation import PlayerInformation
import time
from tkinter import *
from tkinter.ttk import *
from gui import GUI


REGION = Consts.REGIONS['euw']
SUMMONER_NAME = 'the vicugna paco'
API_KEY = ''


def main():
    matchInfo = LiveMatchInfo(region=REGION, summonerName=SUMMONER_NAME, api_key=API_KEY)

    players = [PlayerInformation(matchInfo._playerInfo()[x]) for x in range(10)]
    #player1 = players[1]
    #player1._boughtBootsOfLucidity()
    #player1._boughtBootsOfLucidity()
    #player1.print()
    #player1._usedSummonerSpell(0)





    test = GUI(players)


    '''
    win = Tk()
    win.title('this is a test window')

    lbl1 = Label(win, text = 'label 1')
    lbl2 = Label(win, text = 'label 2')
    lbl3 = Label(win, text = 'label number 3')
    lbl4 = Label(win, text = 'label 4')

    lbl1.grid(column = 0, row = 0, padx = (100,0))
    lbl2.grid(column = 1, row = 0)
    lbl3.grid(column = 0, row = 1, padx = (10,100))
    lbl4.grid(column = 1, row = 1)

    win.mainloop()
    '''







if __name__ == "__main__":
    main()





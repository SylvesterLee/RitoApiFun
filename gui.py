from tkinter import *
import tkinter.ttk
import time


class GUI(object):
    def __init__(self, playersInfo):
        self.team1Members = 0
        self.team2Members = 0

        self.root = Tk()

        self.team1Frame = Frame(self.root)
        self.team1Frame.grid(row = 1, column = 0)

        self.team1Lbl = Label(self.root, text ='Team 1', font = "50").grid(row = 0, column = 0)

        self.team2Frame = Frame(self.root)
        self.team2Frame.grid(row = 1, column = 1)

        self.team2Lbl = Label(self.root, text ='Team 2', font = "50").grid(row = 0, column = 1)

        for player in playersInfo:
            self.createPlayerFrame(player)

        self.root.mainloop()


        '''
        for player in playersInfo:
            summonerNameLbl = Label(self.win, text = 'Summoner Name: ' + player['summonerName'])
            championNameLbl = Label(self.win, text = 'Champion Name: ' + player['champName'])
            summonerSpell1NameLbl = Label(self.win, text = 'Summoner Spell 1: ' + player['summonerSpells'][0])
            summonerSpell2NameLbl = Label(self.win, text = 'Summoner Spell 2: ' + player['summonerSpells'][1])
        '''


    def createPlayerFrame(self, player):
        if player.team == 1:
            frame = self.team1Frame
            teamMembers = self.team1Members
            self.team1Members += 1
        else:
            frame = self.team2Frame
            teamMembers = self.team2Members
            self.team2Members += 1

        Label(frame, text = 'Summoner Name: ' + player.summonerName).grid(row = teamMembers * 4, column = 0)
        Label(frame, text = 'Champion: ' + player.champName).grid(row = teamMembers * 4 + 1, column = 0)
        Label(frame, text = 'Summonerspell 1: ' + player.summonerSpells[0]).grid(row = teamMembers * 4 + 2, column = 0)
        Label(frame, text = 'Summonerspell 2: ' + player.summonerSpells[1]).grid(row = teamMembers * 4 + 3, column = 0)
        Label(frame, text = '-  ' + str(player._getCooldowns()[0])).grid(row = teamMembers * 4 + 2, column = 1)
        Label(frame, text = '-  ' + str(player._getCooldowns()[1])).grid(row = teamMembers * 4 + 3, column = 1)  #padding???

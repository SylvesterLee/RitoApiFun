from tkinter import *
import tkinter.ttk
import time


class GUI(object):
    def __init__(self, playersInfo):
        self.team1Members = 0
        self.team2Members = 0

        self.root = Tk()
        self.root.title("Sylle's Super Awesome Cooldown Counter")

        self.team1Frame = Frame(self.root)
        self.team1Frame.grid(row = 1, column = 0, padx = 50)

        self.team1Lbl = Label(self.root, text ='Team 1', font = "50").grid(row = 0, column = 0, pady = (0, 20))

        self.team2Frame = Frame(self.root)
        self.team2Frame.grid(row = 1, column = 1, padx = 50)

        self.team2Lbl = Label(self.root, text ='Team 2', font = "50").grid(row = 0, column = 1, pady = (0, 20))

        for player in playersInfo:
            self.createPlayerFrame(player)

        self.root.mainloop()

    def createPlayerFrame(self, player):
        PADDING_BETWEEN_PLAYERS = 40
        cdFont = 'Helvetica 13 bold'

        if player.team == 1:
            frame = self.team1Frame
            teamMembers = self.team1Members
            self.team1Members += 1
        else:
            frame = self.team2Frame
            teamMembers = self.team2Members
            self.team2Members += 1

        Label(frame, text = player.summonerName).grid(row = teamMembers * 4, column = 0, sticky="W")
        Label(frame, text = player.champName, font = 'Helvetica 11 bold').grid(row = teamMembers * 4 + 1, column = 0, sticky="W")
        Label(frame, text = player.summonerSpells[0] + ' CD:', font = cdFont).grid(row = teamMembers * 4 + 2, column = 0, sticky="W")
        Label(frame, text = player.summonerSpells[1] + ' CD:', font = cdFont).grid(row = teamMembers * 4 + 3, column = 0, sticky="W", pady = (0, PADDING_BETWEEN_PLAYERS))

        if 'Teleport' in player.summonerSpells:
            Label(frame, text = 'Level:').grid(row = teamMembers * 4, column = 1, sticky="W")
            Entry(frame, width = 4).grid(row = teamMembers * 4, column = 2, sticky="W")

        Label(frame, text = str(player._getCooldowns()[0]), font = cdFont).grid(row = teamMembers * 4 + 2, column = 1, sticky="W")
        Label(frame, text = str(player._getCooldowns()[1]), font = cdFont).grid(row = teamMembers * 4 + 3, column = 1, sticky="W", pady = (0, PADDING_BETWEEN_PLAYERS))

        Checkbutton(frame, text = 'Boots of Lucidity').grid(row = teamMembers * 4 + 1, column = 2, sticky="W")
        Button(frame, text = 'Used ' + player.summonerSpells[0]).grid(row = teamMembers * 4 + 2, column = 2, sticky="W")
        Button(frame, text = 'Used ' + player.summonerSpells[1]).grid(row = teamMembers * 4 + 3, column = 2, sticky="W", pady = (0, PADDING_BETWEEN_PLAYERS))


from tkinter import *
import tkinter.ttk
import time


class GUI(object):
    def __init__(self, playersInfo):
        self.playersInfo = playersInfo
        self.team1Members = 0
        self.team2Members = 0
        self.playerCDLabels = []
        self.playerLevelEntries = []

        self.root = Tk()
        self.root.title("Sylle's Super Awesome Cooldown Counter")

        self.team1Frame = Frame(self.root)
        self.team1Frame.grid(row = 1, column = 0, padx = 50)

        self.team1Lbl = Label(self.root, text ='Team 1', font = "50").grid(row = 0, column = 0, pady = (0, 20))

        self.team2Frame = Frame(self.root)
        self.team2Frame.grid(row = 1, column = 1, padx = 50)

        self.team2Lbl = Label(self.root, text ='Team 2', font = "50").grid(row = 0, column = 1, pady = (0, 20))

        for player in self.playersInfo:
            self.createPlayerFrame(player)

        #self.root.after(1000, self._updateAllPlayers)

        self._updateAllPlayers()
        self.root.mainloop()


    def _updateAllPlayers(self):
        temp = 0
        for idx, CDs in enumerate(self.playerCDLabels):
            self.playersInfo[idx].level = self.playerLevelEntries[idx].get()

            CDs[0].configure(text = int(self.playersInfo[idx]._getCooldowns()[0]))
            CDs[1].configure(text = int(self.playersInfo[idx]._getCooldowns()[1]))

        self.root.after(500, self._updateAllPlayers)

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


        #self.playerLevelEntries.append(entryLevel)
        levelLabel = Label(frame, text = 'Level:')
        entryLevel = IntVar()
        entryLevel.set(1)
        self.playerLevelEntries.append(entryLevel)
        levelEntry = Entry(frame, text = entryLevel, width = 4)

        if 'Teleport' in player.summonerSpells:
            levelLabel.grid(row = teamMembers * 4, column = 1, sticky="W")
            levelEntry.grid(row = teamMembers * 4, column = 2, sticky="W")


        CDLabel1 = Label(frame, text = int(player._getCooldowns()[0]), font = cdFont)
        CDLabel1.grid(row = teamMembers * 4 + 2, column = 1, sticky="W")
        CDlabel2 = Label(frame, text = int(player._getCooldowns()[1]), font = cdFont)
        CDlabel2.grid(row = teamMembers * 4 + 3, column = 1, sticky="W", pady = (0, PADDING_BETWEEN_PLAYERS))
        self.playerCDLabels.append([CDLabel1, CDlabel2])


        hasBootsOfLucidity = BooleanVar(False)
        Checkbutton(frame, text = 'Boots of Lucidity', variable = hasBootsOfLucidity, onvalue = True, offvalue = False, command = lambda: player._boughtBootsOfLucidity(hasBootsOfLucidity)).grid(row = teamMembers * 4 + 1, column = 2, sticky="W")

        Button(frame, text = 'Used ' + player.summonerSpells[0], command = player._usedSummonerSpell1).grid(row = teamMembers * 4 + 2, column = 2, sticky="W")
        Button(frame, text = 'Used ' + player.summonerSpells[1], command = player._usedSummonerSpell2).grid(row = teamMembers * 4 + 3, column = 2, sticky="W", pady = (0, PADDING_BETWEEN_PLAYERS))



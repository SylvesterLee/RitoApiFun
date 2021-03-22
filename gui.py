from tkinter import *
from AutoTyper import AutoTyper


class GUI(object):
    """
    Used for creating and updating the GUI
    """
    def __init__(self, playersInfo):
        """
        Creates the start layout of the GUI

        :param PlayerInformation list playersInfo: list of the relevant player information
        """
        self.playersInfo = playersInfo
        self.team1Members = 0
        self.team2Members = 0
        self.playerCDLabels = []
        self.playerLevelEntries = []
        self.ingameTimerTotalSeconds = 0

        self.root = Tk()
        self.root.title("Sylle's Super Awesome Cooldown Counter")


        self.team1Frame = Frame(self.root)
        self.team1Frame.grid(row = 1, column = 0, padx = 50)

        self.team1Lbl = Label(self.root, text ='Team 1', font = "50").grid(row = 0, column = 0, pady = (0, 20))

        self.team2Frame = Frame(self.root)
        self.team2Frame.grid(row = 1, column = 2, padx = 50)

        self.team2Lbl = Label(self.root, text ='Team 2', font = "50").grid(row = 0, column = 2, pady = (0, 20))

        for player in self.playersInfo:
            self.createPlayerFrame(player)


        self.ingameTimerFrame = Frame(self.root)
        self.ingameTimerFrame.grid(row = 0, column = 1)

        self.createTimerFrame()

        self.autoTyper = AutoTyper()
        self._updateAllPlayers()
        self.root.mainloop()


    def _updateAllPlayers(self):
        """
        Used to update the cooldown labels and levels of each player

        :return: void
        """

        for idx, CDs in enumerate(self.playerCDLabels):
            updatedLvl = self.playerLevelEntries[idx].get()
            if updatedLvl == "":
                updatedLvl = 1
            self.playersInfo[idx].level = int(updatedLvl)

            CDs[0].configure(text = int(self.playersInfo[idx]._getCooldowns()[0]))
            CDs[1].configure(text = int(self.playersInfo[idx]._getCooldowns()[1]))

        self.ingameTimerTotalSeconds += 0.5
        minutes, seconds = self.secondsToMinutes(self.ingameTimerTotalSeconds)
        self.ingameTimerLabel.configure(text = f"{minutes:02}:{seconds:02}")

        self.autoTyper.update_prettyPrintString(self.playersInfo, self.ingameTimerTotalSeconds)
        self.root.after(500, self._updateAllPlayers)


    def createTimerFrame(self):
        """
        used to format and display the ingame timer and to change it manually.
        :return: void
        """
        self.ingameTimerLabelLabel = Label(self.ingameTimerFrame, text = 'Gametime', font = "50")
        self.ingameTimerLabelLabel.grid(row=0, column = 0)

        minutes, seconds = self.secondsToMinutes(self.ingameTimerTotalSeconds)
        self.ingameTimerLabel = Label(self.ingameTimerFrame,text = f"{minutes:02}:{seconds:02}", font = 'Helvetica 13')
        self.ingameTimerLabel.grid(row=0, column = 1)

        self.setTimerFrame = Frame(self.ingameTimerFrame)
        self.setTimerFrame.grid(row = 1, column = 1)

        self.setTimerMinute = Entry(self.setTimerFrame, width = 4)
        self.setTimerMinute.grid(row = 0, column = 0)
        self.timerColon = Label(self.setTimerFrame, text = ":")
        self.timerColon.grid(row = 0, column = 1)
        self.setTimerSecond = Entry(self.setTimerFrame, width = 4)
        self.setTimerSecond.grid(row = 0, column = 2)

        self.ingameSetTimerButton = Button(self.ingameTimerFrame, text = "Set time",
                                           command = lambda : self.setIngameTimerTotalSeconds(self.minutesToSeconds(self.setTimerMinute.get(), self.setTimerSecond.get())))
        self.ingameSetTimerButton.grid(row = 1, column = 0)

    def setIngameTimerTotalSeconds(self, newTotalSeconds):
        try:
            self.ingameTimerTotalSeconds = int(newTotalSeconds)
        except:
            self.ingameTimerTotalSeconds = 0

    def createPlayerFrame(self, player):
        """
        Used to display the relevant information about a player

        :param PlayerInformation player:
        :return: void
        """
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


        levelLabel = Label(frame, text = 'Level:')
        entryLevel = StringVar()
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

    def minutesToSeconds(self, minutes, seconds):
        """

        :param minutes:
        :param seconds:
        :return:
        """
        try:
            return int(minutes) * 60 + int(seconds)
        except:
            print("invalid values in \"set time\"")
        return 0

    def secondsToMinutes(self, secondsTotal):
        """

        :param secondsTotal:
        :return:
        """
        return int(secondsTotal / 60), int(secondsTotal % 60)

from pynput.keyboard import Key, Controller
from pynput import keyboard
import RiotConst as Consts

class AutoTyper(object):
    def __init__(self):
        self.keyboardCtrl = Controller()
        self.prettyPrintString = ""
        self.playersInfo = []
        self.ingameTimerTotalSeconds = 0

        self.listener = keyboard.Listener(
            on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        try:
            if key == keyboard.Key.f12:
                self.printPrettyString()
        except AttributeError:
            print('special key {0} pressed'.format(
                key))


    def update_prettyPrintString(self, playersInfo, ingameTimerTotalSeconds):
        self.playersInfo = playersInfo
        self.ingameTimerTotalSeconds = ingameTimerTotalSeconds

    def printPrettyString(self):
        self.prettyPrintString = ""
        for idx, player in enumerate(self.playersInfo):
            summSpells = player.summonerSpells
            CDs = player._getCooldowns()
            if CDs[0] > 5 and CDs[1] > 5:
                minutes1, seconds1 = self.secondsToMinutes(round(CDs[0] + self.ingameTimerTotalSeconds))
                minutes2, seconds2 = self.secondsToMinutes(round(CDs[1] + self.ingameTimerTotalSeconds))
                self.prettyPrintString += f"{Consts.ChampionShortNames[player.champName]}: {Consts.SummonerShortNames[summSpells[0]]} {minutes1:02}:{seconds1:02}, {Consts.SummonerShortNames[summSpells[1]]} {minutes2:02}:{seconds2:02}. "
            elif CDs[0] > 5:
                minutes1, seconds1 = self.secondsToMinutes(round(CDs[0] + self.ingameTimerTotalSeconds))
                self.prettyPrintString += f"{Consts.ChampionShortNames[player.champName]}: {Consts.SummonerShortNames[summSpells[0]]} {minutes1:02}:{seconds1:02}. "
            elif CDs[1] > 5:
                minutes2, seconds2 = self.secondsToMinutes(round(CDs[1] + self.ingameTimerTotalSeconds))
                self.prettyPrintString += f"{Consts.ChampionShortNames[player.champName]}: {Consts.SummonerShortNames[summSpells[1]]} in {minutes2:02}:{seconds2:02}. "

        self.keyboardCtrl.type(f"{self.prettyPrintString}")

    def secondsToMinutes(self, secondsTotal):
        """

        :param secondsTotal:
        :return:
        """
        return int(secondsTotal / 60), int(secondsTotal % 60)


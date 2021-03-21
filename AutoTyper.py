from pynput.keyboard import Key, Controller
from pynput import keyboard
import RiotConst as Consts

class AutoTyper(object):
    def __init__(self):
        self.keyboardCtrl = Controller()
        self.prettyPrintString = ""
        self.playersInfo = []

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


    def update_prettyPrintString(self, playersInfo):
        self.playersInfo = playersInfo


    def printPrettyString(self):
        self.prettyPrintString = ""
        for idx, player in enumerate(self.playersInfo):
            summSpells = player.summonerSpells
            CDs = player._getCooldowns()
            if CDs[0] > 5 and CDs[1] > 5:
                self.prettyPrintString += f"{Consts.ChampionShortNames[player.champName]}: {Consts.SummonerShortNames[summSpells[0]]} in {round(CDs[0])}, {Consts.SummonerShortNames[summSpells[1]]} in {round(CDs[1])}. "
            elif CDs[0] > 5:
                self.prettyPrintString += f"{Consts.ChampionShortNames[player.champName]}: {Consts.SummonerShortNames[summSpells[0]]} in {round(CDs[0])}. "
            elif CDs[1] > 5:
                self.prettyPrintString += f"{Consts.ChampionShortNames[player.champName]}: {Consts.SummonerShortNames[summSpells[1]]} in {round(CDs[1])}. "

        self.keyboardCtrl.type(f"{self.prettyPrintString}")

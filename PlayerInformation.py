import json
import RiotConst as Consts
import time


class PlayerInformation(object):

    def __init__(self, LiveMatchPlayerInfo):
        self.team = LiveMatchPlayerInfo['team']
        self.summonerName = LiveMatchPlayerInfo['summonerName']
        self.champName = LiveMatchPlayerInfo['champName']
        self.keyStone = LiveMatchPlayerInfo['keyStone']
        self.runes = LiveMatchPlayerInfo['runes']
        self.summonerSpells = LiveMatchPlayerInfo['summonerSpells']
        self.summonerSpellsBaseCD = [self._getBaseSummonerCD(self.summonerSpells[x]) for x in range(2)]
        self.hasCosmicInsight = 'CosmicInsight' in self.runes
        self.hasBootsOfLucidity = False

        self.summonerSpellUsedAt = [time.time()-time.time(), time.time()-time.time()]

    def _getBaseSummonerCD(self, summonerSpell):
        with open('data/summoner.json', encoding='utf8') as json_file:
            data = json.load(json_file)
            for item in data['data'].items():
                if item[1]['name'] == summonerSpell:
                    return item[1]['cooldown'][0]
            print(f"Could not find rune with name: {summonerSpell}")
            return 'NULL'

    def _boughtBootsOfLucidity(self):
        self.hasBootsOfLucidity = True
    def _soldBootsOfLucidity(self):
        self.hasBootsOfLucidity = False

    def _getSummonerSpellCDs(self):
        if self.hasCosmicInsight and self.hasBootsOfLucidity:
            return [i * (1 - Consts.SummonerCooldownReduction['BootsOfLucidityAndCosmicInsight']) for i in self.summonerSpellsBaseCD]
        elif self.hasCosmicInsight:
            return [i * (1 - Consts.SummonerCooldownReduction['CosmicInsight']) for i in self.summonerSpellsBaseCD]
        elif self.hasBootsOfLucidity:
            return [i * (1 - Consts.SummonerCooldownReduction['BootsOfLucidity']) for i in self.summonerSpellsBaseCD]
        else:
            return self.summonerSpellsBaseCD

    def _usedSummonerSpell(self, summonerSpell):      #summonerSpell is either 0 or 1, depending on which summonerspell
        self.summonerSpellUsedAt[summonerSpell] = time.time()

    def _getCooldowns(self):
        return [self._getSummonerSpellCDs()[0] - (time.time() - self.summonerSpellUsedAt[0]), self._getSummonerSpellCDs()[1] - (time.time()-self.summonerSpellUsedAt[1])]


    def print(self):
        print(f"""Team: {self.team}
Summoner Name: {self.summonerName}
Champion Name: {self.champName}
Keystone: {self.keyStone}
Runes: {self.runes}
Summoner Spells: {self.summonerSpells}
Summoner Spell Base Cooldowns: {self.summonerSpellsBaseCD}
Cosmic insight? {self.hasCosmicInsight}
Actual Summoner Spell Cooldown: {self._getSummonerSpellCDs()}""")

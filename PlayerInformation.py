import json
import RiotConst as Consts
import time


class PlayerInformation(object):
    """
    Handles all the information about a player

    Contains attributes for all relevant information pertaining to the cooldown of the
    summoner spells and methods for finding the cooldowns for that player summoner spells.
    """

    def __init__(self, LiveMatchPlayerInfo):
        """
        :param LiveMatchPlayerInfo: A dictionary of all the important information about the player
        """
        self.team = LiveMatchPlayerInfo['team']
        self.summonerName = LiveMatchPlayerInfo['summonerName']
        self.champName = LiveMatchPlayerInfo['champName']
        self.keyStone = LiveMatchPlayerInfo['keyStone']
        self.runes = LiveMatchPlayerInfo['runes']
        self.summonerSpells = LiveMatchPlayerInfo['summonerSpells']
        self.level = 1
        self.summonerSpellsBaseCD = [self._getBaseSummonerCD(self.summonerSpells[x]) for x in range(2)]
        self.hasCosmicInsight = 'CosmicInsight' in self.runes
        self.hasBootsOfLucidity = False

        self.summonerSpellUsedAt = [0, 0]

    def _getBaseSummonerCD(self, summonerSpell):
        """
        Finds the base cooldown of the summoner spell. Every cooldown can be found in the datadragon
        except teleport where we need to have the in RiotConsts.

        :param string summonerSpell: The summoner spell of which we wish to find the base cooldown

        :return: int
                    The cooldown of the summoner spell
        """
        if summonerSpell == 'Teleport':
            return self._getBaseSummonerCDTeleport()
        with open('data/summoner.json', encoding='utf8') as json_file:
            data = json.load(json_file)
            for item in data['data'].items():
                if item[1]['name'] == summonerSpell:
                    return item[1]['cooldown'][0]
            print(f"Could not find rune with name: {summonerSpell}")
            return 'NULL'

    def _boughtBootsOfLucidity(self, answer):
        """
        Used for changing self.hasBootsOfLucidity if a user buys/sells them

        :param bool answer: True/False for if the user has bought it

        :return: void
        """
        self.hasBootsOfLucidity = answer

    def _getSummonerSpellCDs(self):
        """
        Uses the base cooldowns and the constant % cooldown reduction to find the actual cooldowns for each summoner spell

        :return: int list
                    The cooldown of the summoner spells afther cooldown reduction
        """
        summonerSpellCDs = [0, 0]
        for idx, baseCD in enumerate(self.summonerSpellsBaseCD):
            if self.summonerSpells[idx] == 'Teleport':      #Need to calculate a new cd if summonerspell is tp, as it is based on level
                baseCD = self._getBaseSummonerCDTeleport()
            if self.hasCosmicInsight and self.hasBootsOfLucidity:
                summonerSpellCDs[idx] = baseCD * (100/(100 + Consts.SummonerCooldownReduction['BootsOfLucidityAndCosmicInsight']))
            elif self.hasCosmicInsight:
                summonerSpellCDs[idx] = baseCD * (100/(100 + Consts.SummonerCooldownReduction['CosmicInsight']))
            elif self.hasBootsOfLucidity:
                summonerSpellCDs[idx] = baseCD * (100/(100 + Consts.SummonerCooldownReduction['BootsOfLucidity']))
            else:
                summonerSpellCDs[idx] = baseCD
        return summonerSpellCDs

    def _usedSummonerSpell1(self):
        """
        Used summoner spell 1
        :return: void
        """
        self.summonerSpellUsedAt[0] = time.time()

    def _usedSummonerSpell2(self):
        """
        Used summoner spell 2
        :return: void
        """
        self.summonerSpellUsedAt[1] = time.time()

    def _getCooldowns(self): #returns cooldowns at that point in time and makes sure there is no negative values.
        """
        Used to find the remaining cooldown of each summoner spell

        :return: The remaining cooldown of each summoner spell (can not be negative)
        """
        summonerSpell0RemainingCD = self._getSummonerSpellCDs()[0] - (time.time() - self.summonerSpellUsedAt[0])
        summonerSpell1RemainingCD = self._getSummonerSpellCDs()[1] - (time.time() - self.summonerSpellUsedAt[1])
        if summonerSpell0RemainingCD < 0.0 and summonerSpell1RemainingCD < 0.0:
            return [0.0, 0.0]
        elif summonerSpell0RemainingCD < 0.0:
            return [0.0, summonerSpell1RemainingCD]
        elif summonerSpell1RemainingCD < 0.0:
            return [summonerSpell0RemainingCD, 0.0]
        return [summonerSpell0RemainingCD, summonerSpell1RemainingCD]

    def _getBaseSummonerCDTeleport(self):
        """
        Used to find the base cooldown of teleport, based on the player level

        :return: The base cooldown for teleport
        """
        if self.level > 18:
            return Consts.TeleportCooldownPerLevel[18]
        if self.level < 1:
            return Consts.TeleportCooldownPerLevel[1]
        return Consts.TeleportCooldownPerLevel[self.level]

    def print(self):
        """
        Used for testing. Prints all information.

        :return: void
        """
        print(f"""Team: {self.team}
Summoner Name: {self.summonerName}
Champion Name: {self.champName}
Keystone: {self.keyStone}
Runes: {self.runes}
Summoner Spells: {self.summonerSpells}
Summoner Spell Base Cooldowns: {self.summonerSpellsBaseCD}
Cosmic insight? {self.hasCosmicInsight}
Actual Summoner Spell Cooldown: {self._getSummonerSpellCDs()}""")

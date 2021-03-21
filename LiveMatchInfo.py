from riotwatcher import LolWatcher
import json

class LiveMatchInfo(object):
    """
    Gets all the information about the match that the summoner is in using the Riot API
    """

    def __init__(self, region, summonerName, api_key):
        """
        :param string region: The region of the player
        :param string summonerName: The summoner name of the player
        :param string api_key: The API key used for access to the Riot API
        """
        self.region = region
        self.summonerName = summonerName

        self.lolWatcher = LolWatcher(api_key)

    def _getEncryptedSummonerName(self):
        """
        Uses the summoner name of the player to get the encrypted summoner name, which is needed later

        :return: string
                    Encrypted summoner name
        """
        return self.lolWatcher.summoner.by_name(self.region, self.summonerName)


    def _champID_to_champName(self, champID):
        """
        Converts from champion ID to name for later usage

        :param string champID: The champion ID gathered with the Riot API

        :return: string
                    The name of the champion
        """
        with open('data/champion.json', encoding='utf8') as json_file:
            data = json.load(json_file)
            for item in data['data']:
                if int(data['data'][item]['key']) == champID:
                    return data['data'][item]['id']
                    break
            print(f"Could not find champion with id: {champID}")
            return 'Null'

    def _runeID_to_runeName(self, runeID):
        """
        Converts from rune ID to name for later usage

        :param string runeID: The rune ID gathered with the Riot API

        :return: string
                    The name of the rune
        """
        with open('data/runesReforged.json', encoding='utf8') as json_file:
            data = json.load(json_file)
            for item in data:
                for rune in item['slots']:
                    for run in rune['runes']:
                        if run['id'] == runeID:
                            return run['key']
            print(f"Could not find rune with id: {runeID}")
            return 'NULL'

    def _summonerspellID_to_summonerName(self, summonerspellID):
        """
        Converts from summoner spell ID to summoner spell name

        :param string summonerspellID: The summoner spell ID gathered with the Riot API

        :return: string
                    The name of the summoner spell
        """
        with open('data/summoner.json', encoding='utf8') as json_file:
            data = json.load(json_file)
            for item in data['data'].items():
                if int(item[1]['key']) == summonerspellID:
                    return item[1]['name']    ##Maybe this should be 'id'? depends on what to do later
            print(f"Could not find rune with id: {summonerspellID}")
            return 'NULL'


    def _playerInfo(self):
        """
        Takes all of the useful information gathered with the Riot API and turns it into readable information.

        Places it all in a list of dictionaries - each dictionary containing all the important information about a player

        :return: dict list
                    The list of dictionaries containing readable important information about the players
        """
        participantList = []
        liveGameData = self.lolWatcher.spectator.by_summoner(self.region, self._getEncryptedSummonerName()['id'])
        for participant in liveGameData['participants']:
            currentParticipant = {'team':int(participant['teamId']/100),
                                  'summonerName':participant['summonerName'],
                                  'champName':self._champID_to_champName(participant['championId']),
                                  'keyStone':self._runeID_to_runeName(participant['perks']['perkIds'][0]),
                                  'runes':[self._runeID_to_runeName(participant['perks']['perkIds'][x]) for x in range(1,6)],
                                  'summonerSpells':[self._summonerspellID_to_summonerName(participant['spell1Id']), self._summonerspellID_to_summonerName(participant['spell2Id'])]
                                  }
            participantList.append(currentParticipant)

        return participantList

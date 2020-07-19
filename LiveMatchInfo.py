from riotwatcher import LolWatcher
import json

class LiveMatchInfo(object):
    def __init__(self, region, summonerName, api_key):
        self.region = region
        self.summonerName = summonerName

        self.lolWatcher = LolWatcher(api_key)

    def _getEncryptedSummonerName(self):
        return self.lolWatcher.summoner.by_name(self.region, self.summonerName)

    def _champID_to_champName(self, champID):
        with open('data/champion.json', encoding='utf8') as json_file:
            data = json.load(json_file)
            for item in data['data']:
                if int(data['data'][item]['key']) == champID:
                    return data['data'][item]['id']
                    break
            print(f"Could not find champion with id: {champID}")
            return 'Null'

    def _runeID_to_runeName(self, runeID):
        with open('data/runesReforged.json', encoding='utf8') as json_file:
            data = json.load(json_file)
            for item in data:
                for rune in item['slots']:
                    for run in rune['runes']:
                        if run['id'] == runeID:
                            return run['key']
            print(f"Could not find rune with id: {runeID}")
            return 'NULL'

    def _gameInfo(self):
        participantList = []
        liveGameData = self.lolWatcher.spectator.by_summoner(self.region, self._getEncryptedSummonerName()['id'])
        for participant in liveGameData['participants']:
            print(participant)
            currentParticipant = {'team':int(participant['teamId']/100),
                                  'summonerName':participant['summonerName'],
                                  'champName':self._champID_to_champName(participant['championId']),
                                  'keyStone':self._runeID_to_runeName(participant['perks']['perkIds'][0]),
                                  'runes':[self._runeID_to_runeName(participant['perks']['perkIds'][x]) for x in range(1,6)]
                                  }
            participantList.append(currentParticipant)

        return participantList

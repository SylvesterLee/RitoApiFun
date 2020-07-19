from riotwatcher import LolWatcher

class LiveMatchInfo(object):
    def __init__(self, region, summonerName, api_key):
        self.region = region
        self.summonerName = summonerName

        self.lolWatcher = LolWatcher(api_key)

    def _getEncryptedSummonerName(self):
        return self.lolWatcher.summoner.by_name(self.region, self.summonerName)

    def _gameInfo(self):
        return self.lolWatcher.spectator.by_summoner(self.region, self._getEncryptedSummonerName()['id'])

import RiotConst as Consts
from riotwatcher import LolWatcher, ApiError
from LiveMatchInfo import LiveMatchInfo
import json

REGION = Consts.REGIONS['euw']
SUMMONER_NAME = 'Dawidsonek'
API_KEY = 'RGAPI-e25dd653-37f8-4941-a4de-2f0555b0f33c'


def main():
    matchInfo = LiveMatchInfo(region=REGION, summonerName=SUMMONER_NAME, api_key=API_KEY)
    print(matchInfo._playerInfo())


if __name__ == "__main__":
    main()



'''
get summoner id med get_summoner_by_name.
Den kan bruges med spectater/activegames for at få rune id og summoner spells


'''

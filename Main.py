import RiotConst as Consts
from riotwatcher import LolWatcher, ApiError
from LiveMatchInfo import LiveMatchInfo
import json

REGION = Consts.REGIONS['euw']
SUMMONER_NAME = 'IlIlIlIIIlIIIll'
API_KEY = 'RGAPI-74a53027-2856-414d-870f-44d944107770'


def main():
    matchInfo = LiveMatchInfo(region=REGION, summonerName=SUMMONER_NAME, api_key=API_KEY)
    print(matchInfo._gameInfo())


if __name__ == "__main__":
    main()



'''
get summoner id med get_summoner_by_name.
Den kan bruges med spectater/activegames for at få rune id og summoner spells


'''

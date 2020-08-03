import RiotConst as Consts
from LiveMatchInfo import LiveMatchInfo
from PlayerInformation import PlayerInformation
from gui import GUI


REGION = Consts.REGIONS['euw']
SUMMONER_NAME = 'MRS JaVaáa'
API_KEY = 'RGAPI-d2a17467-eb44-4d02-bbe6-b2e0ee0ac5a4'


def main():
    matchInfo = LiveMatchInfo(region=REGION, summonerName=SUMMONER_NAME, api_key=API_KEY)

    players = [PlayerInformation(matchInfo._playerInfo()[x]) for x in range(10)]

    GUIwindow = GUI(players)


if __name__ == "__main__":
    main()





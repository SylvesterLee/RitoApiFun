import RiotConst as Consts
from LiveMatchInfo import LiveMatchInfo
from PlayerInformation import PlayerInformation
from gui import GUI
import AutoTyper


REGION = Consts.REGIONS['euw']
SUMMONER_NAME = 's1 night'
API_KEY = 'RGAPI-7f45cd1d-a6a3-4945-b4a4-dbe85a32700d'


def main():
    matchInfo = LiveMatchInfo(region=REGION, summonerName=SUMMONER_NAME, api_key=API_KEY)

    players = [PlayerInformation(matchInfo._playerInfo()[x]) for x in range(10)]

    GUIwindow = GUI(players)


if __name__ == "__main__":
    main()

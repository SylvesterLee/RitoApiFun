import RiotConst as Consts
from LiveMatchInfo import LiveMatchInfo
from PlayerInformation import PlayerInformation
from gui import GUI
import AutoTyper


REGION = Consts.REGIONS['euw']
SUMMONER_NAME = 'rule aizhon'
API_KEY = 'RGAPI-e5886c9d-c795-407e-853c-9a2853c94152'


def main():
    matchInfo = LiveMatchInfo(region=REGION, summonerName=SUMMONER_NAME, api_key=API_KEY)

    players = [PlayerInformation(matchInfo._playerInfo()[x]) for x in range(10)]

    GUIwindow = GUI(players)


if __name__ == "__main__":
    main()

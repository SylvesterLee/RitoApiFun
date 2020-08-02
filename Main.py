import RiotConst as Consts
from LiveMatchInfo import LiveMatchInfo
from PlayerInformation import PlayerInformation
from gui import GUI


REGION = Consts.REGIONS['euw']
SUMMONER_NAME = 'Kakudos'
API_KEY = ''


def main():
    matchInfo = LiveMatchInfo(region=REGION, summonerName=SUMMONER_NAME, api_key=API_KEY)

    players = [PlayerInformation(matchInfo._playerInfo()[x]) for x in range(10)]

    GUIwindow = GUI(players)


if __name__ == "__main__":
    main()





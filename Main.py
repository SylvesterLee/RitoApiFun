import RiotConst as Consts
from LiveMatchInfo import LiveMatchInfo
from PlayerInformation import PlayerInformation

REGION = Consts.REGIONS['euw']
SUMMONER_NAME = 'Kobbe'
API_KEY = 'RGAPI-5a2dc19f-0f80-4b1c-9385-eb8d2bd66172'


def main():
    matchInfo = LiveMatchInfo(region=REGION, summonerName=SUMMONER_NAME, api_key=API_KEY)

    player1 = PlayerInformation(matchInfo._playerInfo()[2])
    player1._boughtBootsOfLucidity()
    player1.print()

if __name__ == "__main__":
    main()





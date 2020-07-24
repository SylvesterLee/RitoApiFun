import RiotConst as Consts
from LiveMatchInfo import LiveMatchInfo
from PlayerInformation import PlayerInformation
import time
#from gui import testFun


REGION = Consts.REGIONS['euw']
SUMMONER_NAME = 'Rip in Peace DFG'
API_KEY = 'RGAPI-01d1b3c4-013f-4f38-af8b-651d6ced1cfb'


def main():
    matchInfo = LiveMatchInfo(region=REGION, summonerName=SUMMONER_NAME, api_key=API_KEY)

    #players = [PlayerInformation(matchInfo._playerInfo()[x]) for x in range(10)]
    player1 = PlayerInformation(matchInfo._playerInfo()[0])
    player1._boughtBootsOfLucidity()
    player1.print()

    player1._usedSummonerSpell(0)
    player1._usedSummonerSpell(1)
    time.sleep(161)
    print(player1._getCooldowns())





    #for player in players:
    #    player.print()







if __name__ == "__main__":
    main()





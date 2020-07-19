import RiotConst as Consts
from riotwatcher import LolWatcher, ApiError

REGION = Consts.REGIONS['euw']
SUMMONER_NAME = 'agrsv'
API_KEY = 'RGAPI-74a53027-2856-414d-870f-44d944107770'


def main():

    #response = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata',verify=False)
    #print(response.json())


    lolWatcher = LolWatcher(API_KEY)

    me = lolWatcher.summoner.by_name(REGION, SUMMONER_NAME)

    gameInfo = lolWatcher.spectator.by_summoner(REGION, me['id'])
    print(gameInfo)



if __name__ == "__main__":
    main()



'''
get summoner id med get_summoner_by_name.
Den kan bruges med spectater/activegames for at få rune id og summoner spells


'''

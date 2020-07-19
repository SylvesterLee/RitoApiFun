import RiotConst as Consts
from riotwatcher import LolWatcher, ApiError
from LiveMatchInfo import LiveMatchInfo
import json

REGION = Consts.REGIONS['euw']
SUMMONER_NAME = 'FB HolyPhoenîx'
API_KEY = 'RGAPI-74a53027-2856-414d-870f-44d944107770'


def main():

    #response = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata',verify=False)
    #print(response.json())

    matchInfo = LiveMatchInfo(region=REGION, summonerName=SUMMONER_NAME, api_key=API_KEY)
    print(matchInfo._gameInfo())

    '''
    champID = 142
    foundChampName = False
    with open('Champions.json', encoding='utf8') as json_file:
        data = json.load(json_file)
        for item in data['data']:
            if int(data['data'][item]['key']) == champID:
                champName = data['data'][item]['id']
                foundChampName = True
                break
        if not foundChampName:
            print(f"Could not find champion with id: champID")
            champName = 'Null'
        else:
            print(champName)
            '''

if __name__ == "__main__":
    main()



'''
get summoner id med get_summoner_by_name.
Den kan bruges med spectater/activegames for at få rune id og summoner spells


'''

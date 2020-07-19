from RiotAPI import RiotAPI

def main():
    api = RiotAPI('RGAPI-74a53027-2856-414d-870f-44d944107770')
    r = api.get_summoner_by_name('Kakudos')
    print(r)

if __name__ == "__main__":
    main()

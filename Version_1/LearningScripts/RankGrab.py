from riotwatcher import LolWatcher

region = str(input("Your region : ")) #If you only need EUW, just do region = "euw1"
summonerName = str(input("Your summonername : ")) #Asking for the user's summoner name
watcher = LolWatcher(api_key="RGAPI-61431001-085c-4f28-a2aa-f9f4b68b3136")
try:
    summonner = watcher.summoner.by_name(region=region, summoner_name=summonerName) #Getting account informations, you can print(summoner) to see what it gives
    rank = watcher.league.by_summoner(region=region, encrypted_summoner_id=summonner["id"]) #User ranks using his id in summoner
except:
    print("Incorret Summoner Name.")


tier = rank[0]["tier"]
ranklol = rank[0]["rank"]
lp = rank[0]["leaguePoints"]

print(f"{tier} {ranklol} {lp} LP")

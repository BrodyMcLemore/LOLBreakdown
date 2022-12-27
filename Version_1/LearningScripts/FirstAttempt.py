from riotwatcher import LolWatcher, ApiError
import pandas as pd
import json
import openpyxl

MyKey = "RGAPI-61431001-085c-4f28-a2aa-f9f4b68b3136"
MyReg = "na1"
watcher = LolWatcher(MyKey)
MyAccount = watcher.summoner.by_name(MyReg, "ChaoticThunder0")

MyMatches = watcher.match.matchlist_by_puuid(MyReg, MyAccount["puuid"])
LastMatchID = MyMatches[0]

MatchDetail = watcher.match.by_id(MyReg,LastMatchID)
Output =[]
#print(MatchDetail["metadata"]['participants'])
#print("-----")
count = 0
while count <= 9:
    dict= {
    "Player Name" : MatchDetail["info"]['participants'][count]["summonerName"],
    "Postition" : MatchDetail["info"]['participants'][count]["individualPosition"],
    "Champion" : MatchDetail["info"]['participants'][count]["championName"],
    "Kills" : MatchDetail["info"]['participants'][count]["kills"],
    "Deaths" : MatchDetail["info"]['participants'][count]["deaths"],
    "Assists" : MatchDetail["info"]['participants'][count]["assists"]
    }
    df = pd.DataFrame(dict, index=[count])
    print(df)
    count +=1
df.to_excel("GoodOutput.xlsx")

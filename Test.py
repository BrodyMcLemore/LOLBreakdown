from Project_Files.config import API_KEY
from Project_Files.DictCalls import RuneDict, GetCurrentVersion
from riotwatcher import LolWatcher

watcher = LolWatcher(API_KEY)
AccountInfo = watcher.summoner.by_name("na1", "ChaoticThunder0")
MatchList = watcher.match.matchlist_by_puuid("na1", AccountInfo["puuid"])
MatchDetail = watcher.match.by_id("na1", MatchList[0])

Runes = RuneDict(GetCurrentVersion())

for y in range(3):
    for x in range(3):
        for z in range(3):
            try:
                print(Runes[str(MatchDetail["info"]["participants"][z]["perks"]["styles"][y]["selections"][x]["perk"])])
            except:
                print("Failed")
                continue

# [{'description': 'primaryStyle', 
# 'selections': 
#     [{'perk': 8008, 'var1': 76, 'var2': 10, 'var3': 0}, 
#     {'perk': 8009, 'var1': 2323, 'var2': 0, 'var3': 0}, 
#     {'perk': 9103, 'var1': 8, 'var2': 50, 'var3': 0}, 
#     {'perk': 8014, 'var1': 433, 'var2': 0, 'var3': 0}], 
#     'style': 8000}, 
# {'description': 'subStyle', 
# 'selections': 
#     [{'perk': 8233, 'var1': 5, 'var2': 20, 'var3': 0}, 
#     {'perk': 8236, 'var1': 14, 'var2': 0, 'var3': 0}], 
#     'style': 8200}]

from urllib.request import urlopen
import json

class  MakeDict(dict): 
    def __init__(self): 
        self = dict() 
          
    def add(self, key, value): 
        self[key] = value 

def GetCurrentVersion():
    return json.loads(urlopen("https://ddragon.leagueoflegends.com/api/versions.json").read())[0]

def SummonerSpellDict(CurrentVersion):
    SummonerSpellsDict = MakeDict()
    ListSummonerSpells = json.loads(urlopen("https://ddragon.leagueoflegends.com/cdn/"+str(CurrentVersion)+"/data/en_US/summoner.json").read())["data"]
    for key_, value in ListSummonerSpells.items():
        SummonerSpellsDict.key = ListSummonerSpells[key_]["key"]
        SummonerSpellsDict.value = ListSummonerSpells[key_]["name"]
        SummonerSpellsDict.add(SummonerSpellsDict.key,SummonerSpellsDict.value)
    return SummonerSpellsDict

def ItemDict(CurrentVersion):
    ItemsDict = MakeDict()
    ListItems = json.loads(urlopen("https://ddragon.leagueoflegends.com/cdn/"+str(CurrentVersion)+"/data/en_US/item.json").read())["data"]
    for i in range(1001,8021):
        try:
            ItemsDict.key = str(i)
            ItemsDict.value = ListItems[str(i)]["name"]
            ItemsDict.add(ItemsDict.key, ItemsDict.value)
        except:
            continue
    return ItemsDict

def RuneDict(CurrentVersion):
    RunesDict = MakeDict()
    ListRunes = json.loads(urlopen("https://ddragon.leagueoflegends.com/cdn/"+str(CurrentVersion)+"/data/en_US/runesReforged.json").read())
    for y in range(5):
        for x in range(5):
         for z in range(5):
            try:
                RunesDict.key = str(ListRunes[y]["slots"][x]["runes"][z]["id"])
                RunesDict.value = str(ListRunes[y]["slots"][x]["runes"][z]["name"])
                RunesDict.add(RunesDict.key, RunesDict.value)
            except:
                continue
    return RunesDict
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


RuneDict = {
"8112" : "Electrocute",
"8124" : "Predator",
"8128" : "Dark Harvest",
"9923" : "Hail of Blades",
"8351" : "Glacial Augment",
"8360" : "Unsealed Spellbook",
"8369" : "First Strike",
"8005" : "Press the Attack",
"8008" : "Lethal Tempo",
"8021" : "Fleet Footwork",
"8010" : "Conqueror",
"8437" : "Grasp of the Undying",
"8439" : "Aftershock",
"8465" : "Guardian",
"8214" : "Summon Aery",
"8229" : "Arcane Comet",
"8230" : "Phase Rush"
}
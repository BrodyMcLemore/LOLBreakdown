from urllib.request import urlopen
import ssl
import json
import os
import getpass


ssl._create_default_https_context = ssl._create_unverified_context


class MakeDict(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

def GetCurrentVersion():
    return json.loads(urlopen("https://ddragon.leagueoflegends.com/api/versions.json").read())[0]

def MakeSummonerSpellDict(CurrentVersion):
    SummonerSpellsDict = MakeDict()
    ListSummonerSpells = json.loads(urlopen("https://ddragon.leagueoflegends.com/cdn/"+str(
        CurrentVersion)+"/data/en_US/summoner.json").read())["data"]
    for key_, value in ListSummonerSpells.items():
        SummonerSpellsDict.key = ListSummonerSpells[key_]["key"]
        SummonerSpellsDict.value = ListSummonerSpells[key_]["name"]
        SummonerSpellsDict.add(SummonerSpellsDict.key,
                               SummonerSpellsDict.value)
    return SummonerSpellsDict


def MakeItemDict(CurrentVersion):
    ItemsDict = MakeDict()
    ListItems = json.loads(urlopen("https://ddragon.leagueoflegends.com/cdn/" +
                           str(CurrentVersion)+"/data/en_US/item.json").read())["data"]
    for i in range(1001, 8021):
        try:
            ItemsDict.key = str(i)
            ItemsDict.value = ListItems[str(i)]["name"]
            ItemsDict.add(ItemsDict.key, ItemsDict.value)
        except:
            continue
    return ItemsDict


def MakeRuneDict(CurrentVersion):
    RunesDict = MakeDict()
    ListRunes = json.loads(urlopen("https://ddragon.leagueoflegends.com/cdn/" +
                           str(CurrentVersion)+"/data/en_US/runesReforged.json").read())
    for y in range(5):
        for x in range(5):
            for z in range(5):
                try:
                    RunesDict.key = str(
                        ListRunes[y]["slots"][x]["runes"][z]["id"])
                    RunesDict.value = str(
                        ListRunes[y]["slots"][x]["runes"][z]["name"])
                    RunesDict.add(RunesDict.key, RunesDict.value)
                except:
                    continue
    return RunesDict

def MakeProgramFiles():
    path = os.path.join(os.getenv("APPDATA"), "LOLBreakdown")
    if not os.path.exists(path):
        os.mkdir(path)

    CurrentVersionFilePath = os.path.join(path, "CurrentVersion.json")
    SummonerSpellsFilePath = os.path.join(path, "SummonerSpells.json")
    ItemsFilePath = os.path.join(path, "Items.json")
    RunesFilePath = os.path.join(path, "Runes.json")

    listOfPaths = [
        CurrentVersionFilePath,
        SummonerSpellsFilePath,
        ItemsFilePath,
        RunesFilePath
        ]

    for _file in listOfPaths:
        if not os.path.exists(_file):
            file = open(_file, "w+")
            file.close()
        
    with open(CurrentVersionFilePath, "r+") as CurrentVersionFile:
        try:
            localVersion = json.load(CurrentVersionFile)[0]
            onlineVersion = json.loads(urlopen("https://ddragon.leagueoflegends.com/api/versions.json").read())[0]
        except:
            data = json.loads(urlopen("https://ddragon.leagueoflegends.com/api/versions.json").read())
            json.dump(data ,CurrentVersionFile, indent=1)
            localVersion = data[0]
            onlineVersion = json.loads(urlopen("https://ddragon.leagueoflegends.com/api/versions.json").read())[0]
            json.dump(MakeSummonerSpellDict(onlineVersion), open(SummonerSpellsFilePath, "r+"), indent=1)
            json.dump(MakeItemDict(onlineVersion), open(ItemsFilePath, "r+"), indent=1)
            json.dump(MakeRuneDict(onlineVersion), open(RunesFilePath, "r+"), indent=1)


        if localVersion != onlineVersion:
            onlineData = json.loads(urlopen("https://ddragon.leagueoflegends.com/api/versions.json").read())
            json.dump(onlineData ,CurrentVersionFile, indent=1)
            json.dump(MakeSummonerSpellDict(onlineVersion), open(SummonerSpellsFilePath, "r+"), indent=1)
            json.dump(MakeItemDict(onlineVersion), open(ItemsFilePath, "r+"), indent=1)
            json.dump(MakeRuneDict(onlineVersion), open(RunesFilePath, "r+"), indent=1)




def GetSummonerSpellDict():
    path = os.path.join(os.getenv("APPDATA"), "LOLBreakdown", "SummonerSpells.json")
    SummonerSpells = json.load(open(path, "r+"))
    return SummonerSpells


def GetItemDict():
    path = os.path.join(os.getenv("APPDATA"), "LOLBreakdown", "Items.json")
    Items = json.load(open(path, "r+"))
    return Items
    
def GetRuneDict():
    path = os.path.join(os.getenv("APPDATA"), "LOLBreakdown", "Runes.json")
    Runes = json.load(open(path, "r+"))
    return Runes
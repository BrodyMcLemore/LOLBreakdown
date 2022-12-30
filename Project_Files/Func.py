from Project_Files.BoilerPlate import MakeBoilerPlateCells
from openpyxl import Workbook
from riotwatcher import LolWatcher
import os
from Project_Files.DictCalls import *
from tkinter import ttk


def SaveBook(Workbook, PlayerName):
    wb = Workbook
    if not os.path.exists(os.getcwd()+"/Output"):
        os.mkdir(str(os.getcwd()+"/Output"))
        try:
            wb.save(str(os.getcwd())+"/Output/" + PlayerName + ".xlsx")
            return "Success"
        except:
            return "Fail"
    else:
        try:
            wb.save(str(os.getcwd())+"/Output/" + PlayerName + ".xlsx")
            return "Success"
        except:
            return "Fail"


def OutputGames(Region, MatchList, GameCount, Row, CallValues, Watcher, Workbook,PlayerName, CurrentVersion):
    watcher = Watcher
    wb = Workbook
    wb.create_sheet(str(PlayerName))
    while GameCount <= 17:
        MatchDetail = watcher.match.by_id(Region, MatchList[GameCount])
        if MatchDetail["info"]["gameMode"] == "CLASSIC":
            MakeBoilerPlateCells(wb[str(PlayerName)], Row, MatchDetail,CallValues)
            OutputRed(wb[str(PlayerName)], MatchDetail, Row, CallValues, CurrentVersion)
            OutputBlue(wb[str(PlayerName)], MatchDetail, Row, CallValues, CurrentVersion)
            Row += 8
        GameCount += 1
    del wb["Sheet"]



def OutputRed(worksheet, MatchDetail, startRow, CallValues, CurrentVersion):
    ws = worksheet
    StartWorkRow = startRow + 3
    for row in range(5):
        for col in range(len(CallValues)):
            if CallValues[col] == "kills":
                CalledValue = ws.cell(StartWorkRow+row, col+1)
                Kills = str(MatchDetail["info"]['participants'][row]["kills"])
                Deaths = str(MatchDetail["info"]
                             ['participants'][row]["deaths"])
                Assists = str(MatchDetail["info"]
                              ['participants'][row]["assists"])
                CalledValue.value = Kills + "/" + Deaths + "/" + Assists

            elif CallValues[col] == "inventory":
                Items = ["item0","item1","item2","item3","item4","item5"]
                ItemNames =[]
                ItemsDict = ItemDict(CurrentVersion)
                CalledValue = ws.cell(StartWorkRow+row, col+1)
                for i in range(5):
                    if str(MatchDetail["info"]['participants'][row][Items[i]]) != "0":
                        ItemNames.append(ItemsDict[str(MatchDetail["info"]['participants'][row][Items[i]])])
                CalledValue.value = str(str(", ".join(ItemNames)))

            elif CallValues[col] == "summonerSpells":
                SummonerSpells = SummonerSpellDict(CurrentVersion)
                CalledValue = ws.cell(StartWorkRow+row, col+1)
                CalledValue.value = str(SummonerSpells[str(MatchDetail["info"]['participants'][row]["summoner1Id"])]) +" and "+ str(SummonerSpells[str(MatchDetail["info"]['participants'][row+5]["summoner2Id"])])
            
            elif CallValues[col] == "runes":
                RunesDict = RuneDict(CurrentVersion)
                CalledValue = ws.cell(StartWorkRow+row, col+1)
                Runes = []
                for y in range(3):
                    for x in range(4):
                        try:
                            Runes.append(RunesDict[str(MatchDetail["info"]["participants"][row]["perks"]["styles"][y]["selections"][x]["perk"])])
                        except:
                            continue
                CalledValue.value = str(Runes[0] + " and "+ Runes[4])
            else:
                CalledValue = ws.cell(StartWorkRow+row, col+1)
                CalledValue.value = MatchDetail["info"]['participants'][row][CallValues[col]]



def OutputBlue(worksheet, MatchDetail, startRow, CallValues, CurrentVersion):
    ws = worksheet
    StartWorkRow = startRow + 3
    for row in range(5):
        for col in range(len(CallValues)):
            if CallValues[col] == "kills":
                CalledValue = ws.cell(StartWorkRow+row, col+2+len(CallValues))
                Kills = str(MatchDetail["info"]['participants'][row+5]["kills"])
                Deaths = str(MatchDetail["info"]
                             ['participants'][row+5]["deaths"])
                Assists = str(MatchDetail["info"]
                              ['participants'][row+5]["assists"])
                CalledValue.value = Kills + "/" + Deaths + "/" + Assists

            elif CallValues[col] == "inventory":
                Items = ["item0","item1","item2","item3","item4","item5"]
                ItemNames =[]
                ItemsDict = ItemDict(CurrentVersion)
                CalledValue = ws.cell(StartWorkRow+row, col+2+len(CallValues))
                for i in range(5):
                    if str(MatchDetail["info"]['participants'][row+5][Items[i]]) != "0":
                        ItemNames.append(ItemsDict[str(MatchDetail["info"]['participants'][row+5][Items[i]])])
                CalledValue.value = str(str(", ".join(ItemNames)))

            elif CallValues[col] == "summonerSpells":
                SummonerSpells = SummonerSpellDict(CurrentVersion)
                CalledValue = ws.cell(StartWorkRow+row, col+2+len(CallValues))
                CalledValue.value = str(SummonerSpells[str(MatchDetail["info"]['participants'][row+5]["summoner1Id"])]) +" and "+ str(SummonerSpells[str(MatchDetail["info"]['participants'][row+5]["summoner2Id"])])
            
            elif CallValues[col] == "runes":
                RunesDict = RuneDict(CurrentVersion)
                CalledValue = ws.cell(StartWorkRow+row, col+2+len(CallValues))
                Runes = []
                for y in range(3):
                    for x in range(4):
                        try:
                            Runes.append(RunesDict[str(MatchDetail["info"]["participants"][row+5]["perks"]["styles"][y]["selections"][x]["perk"])])
                        except:
                            continue
                CalledValue.value = str(Runes[0] + " and "+ Runes[4])
            else:
                CalledValue = ws.cell(StartWorkRow+row, col+2+len(CallValues))
                CalledValue.value = MatchDetail["info"]['participants'][row+5][CallValues[col]]
                

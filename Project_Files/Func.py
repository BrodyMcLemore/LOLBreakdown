from Project_Files.BoilerPlate import MakeBoilerPlateCells
from openpyxl import Workbook
from riotwatcher import LolWatcher
import os


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


def OutputGames(Region, MatchList, GameCount, Row, CallValues, Watcher, Workbook,PlayerName):
    watcher = Watcher
    wb = Workbook
    wb.create_sheet(str(PlayerName))
    while GameCount <= 17:
        MatchDetail = watcher.match.by_id(Region, MatchList[GameCount])
        if MatchDetail["info"]["gameMode"] == "CLASSIC":
            MakeBoilerPlateCells(wb[str(PlayerName)], Row, MatchDetail,CallValues)
            OutputRed(wb[str(PlayerName)], MatchDetail, Row, CallValues)
            OutputBlue(wb[str(PlayerName)], MatchDetail, Row, CallValues)
            Row += 8
        GameCount += 1
    del wb["Sheet"]



def OutputRed(worksheet, MatchDetail, startRow, CallValues):
    ws = worksheet
    StartWorkRow = startRow + 3
    for row in range(5):
        for col in range(len(CallValues)):
            if CallValues[col] != "kills":
                CalledValue = ws.cell(StartWorkRow+row, col+1)
                CalledValue.value = MatchDetail["info"]['participants'][row][CallValues[col]]
            else:
                CalledValue = ws.cell(StartWorkRow+row, col+1)
                Kills = str(MatchDetail["info"]['participants'][row]["kills"])
                Deaths = str(MatchDetail["info"]
                             ['participants'][row]["deaths"])
                Assists = str(MatchDetail["info"]
                              ['participants'][row]["assists"])
                CalledValue.value = Kills + "/" + Deaths + "/" + Assists


def OutputBlue(worksheet, MatchDetail, startRow, CallValues):
    ws = worksheet
    StartWorkRow = startRow + 3
    for row in range(5):
        for col in range(len(CallValues)):
            if CallValues[col] != "kills":
                CalledValue = ws.cell(StartWorkRow+row, col+2+len(CallValues))
                CalledValue.value = MatchDetail["info"]['participants'][row +
                                                                        5][CallValues[col]]
            else:
                CalledValue = ws.cell(StartWorkRow+row, col+2+len(CallValues))
                Kills = str(MatchDetail["info"]
                            ['participants'][row+5]["kills"])
                Deaths = str(MatchDetail["info"]
                             ['participants'][row+5]["deaths"])
                Assists = str(MatchDetail["info"]
                              ['participants'][row+5]["assists"])
                CalledValue.value = Kills + "/" + Deaths + "/" + Assists

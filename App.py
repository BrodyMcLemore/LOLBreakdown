from tkinter import *
from tkinter import ttk, messagebox
from Project_Files.Func import OutputGames, SaveBook
from openpyxl import Workbook
from riotwatcher import LolWatcher
from Project_Files.config import API_KEY
from Project_Files.DictCalls import GetCurrentVersion
import os 


# Top Level Window handling
# Making the Window
MainWin = Tk()
MainWin.title("LOL Breakdown")
MainWin.resizable(width=False, height=False)
MainWin.geometry("500x250")
BaseDir = os.path.dirname(__file__)
MainWin.iconbitmap(os.path.join(BaseDir,"Icons","Logo.ico"))

# Handling the Frame
MainFrame = Frame(MainWin)
MainFrame.pack(padx=10, pady=10)
MainFrame.grid(column=0, row=0, sticky="NW")

# Setting Global Variables
# App Variables
PlayerName = StringVar()
RegionVal = StringVar(value="North America")
SummonerName = IntVar(value=1)
ChampionName = IntVar(value=1)
KDA = IntVar(value=0)
Roll = IntVar(value=0)
Level = IntVar(value=0)
Runes = IntVar(value=0)
TotalDamage = IntVar(value=0)
VisionScore = IntVar(value=0)
SummonerSpells = IntVar(value=0)
CreepScore = IntVar(value=0)
Items = IntVar(value=0)
GameResult = IntVar(value=0)


# Working Variables and Dictionaries 
# Working Dictionaries 
RegionCommon = [
    "North America",
    "Brazil",
    "Europe Nordic & East",
    "Europe West",
    "Latin America North",
    "Latin America South",
    "Oceania",
    "Russia",
    "Turkey",
    "Japan"
]
RegionServer = {
    "North America": "na1",
    "Brazil": "br1",
    "Europe Nordic & East": "eun1",
    "Europe West": "euw1",
    "Latin America North": "la1",
    "Latin America South": "la2",
    "Oceania": "oc1",
    "Russia": "ru",
    "Turkey": "tr1",
    "Japan": "jp1"
}
VariableCall = {
    "SummonerName": "summonerName",
    "ChampionName": "championName",
    "KDA": "KDA",
    "Roll": "teamPosition",
    "Level": "champLevel",
    "Runes": "runes",
    "TotalDamage": "totalDamageDealt",
    "VisionScore": "visionScore",
    "SummonerSpells": "summonerSpells",
    "CreepScore": "creepScore",
    "Items": "inventory",
    "GameResult" : "gameResult"
}

# Working Variables 
GameCount = 0
Row = 1
watcher = LolWatcher(API_KEY)


# Functions and Backend
try:
    from ctypes import windll
    myappid = "LOLBreakdown"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

def GetCallVal():
    CallValues = []
    if SummonerName.get() == 1:
        CallValues.append(VariableCall["SummonerName"])
    if ChampionName.get() == 1:
        CallValues.append(VariableCall["ChampionName"])
    if KDA.get() == 1:
        CallValues.append(VariableCall["KDA"])
    if Roll.get() == 1:
        CallValues.append(VariableCall["Roll"])
    if Level.get() == 1:
        CallValues.append(VariableCall["Level"])
    if Runes.get() == 1:
        CallValues.append(VariableCall["Runes"])
    if TotalDamage.get() == 1:
        CallValues.append(VariableCall["TotalDamage"])
    if VisionScore.get() == 1:
        CallValues.append(VariableCall["VisionScore"])
    if SummonerSpells.get() == 1:
        CallValues.append(VariableCall["SummonerSpells"])
    if CreepScore.get() == 1:
        CallValues.append(VariableCall["CreepScore"])
    if Items.get() == 1:
        CallValues.append(VariableCall["Items"])
    if GameResult.get() == 1:
        CallValues.append(VariableCall["GameResult"])
    return CallValues


def Run():
    Region = RegionServer[RegionVal.get()]
    AccountName = PlayerName.get()
    try:
        AccountInfo = watcher.summoner.by_name(Region, AccountName)
    except:
        messagebox.showerror(
            "Name Error", "The Player Name you have entered is not valid, please try again.")
        return
    MatchList = watcher.match.matchlist_by_puuid(Region, AccountInfo["puuid"])
    if len(GetCallVal()) <= 0:
        messagebox.showerror(
            "Failure", "You did not select any data options, please select at least 1 and try again.")
    else:
        wb = Workbook()
        OutputGames(Region, MatchList, GameCount, Row, GetCallVal(),
                    watcher, wb, AccountName, GetCurrentVersion())
        if SaveBook(wb, AccountName) == "Success":
            messagebox.showinfo(
                "Success", "Your Game Data has been saved to Output/"+AccountName)
        elif SaveBook(wb, AccountName) == "Fail":
            messagebox.showerror(
                "Failure", "Your Game Data did NOT save correctly, please close the file and try again.")


# Building the Front End
# Player Name and Region Labels and Entries
PlayerNameLabel = ttk.Label(MainFrame, text="Key Player Name:", font=(
    'calibre', 12, 'bold'), anchor="center", takefocus=True)
RegionLabel = ttk.Label(MainFrame, text="Region:", font=(
    'calibre', 12, 'bold'), justify="left", anchor="center")
PlayerNameEntry = ttk.Entry(
    MainFrame, textvariable=PlayerName, font=('calibre', 10, 'normal'))
RegionComboBox = ttk.Combobox(MainFrame, textvariable=RegionVal,
                              values=RegionCommon, state="readonly", font=('calibre', 10, 'normal'))
ProgressBar = ttk.Progressbar(
    MainFrame, orient="horizontal", length=300, mode='determinate')

# CallValue Checkboxes and Label
CallValuesLabel = ttk.Label(MainFrame, text="Reported Values", font=(
    'calibre', 12, 'bold'), anchor="center")
SummonerNameBox = ttk.Checkbutton(
    MainFrame, text="Summoner Name", variable=SummonerName)
ChampionNameBox = ttk.Checkbutton(
    MainFrame, text="Champion Name", variable=ChampionName)
KDABox = ttk.Checkbutton(MainFrame, text="KDA", variable=KDA)
RollBox = ttk.Checkbutton(MainFrame, text="Position", variable=Roll)
LevelBox = ttk.Checkbutton(MainFrame, text="Champion Level", variable=Level)
RunesBox = ttk.Checkbutton(
    MainFrame, text="Primary and Secondary Runes", variable=Runes)
TotalDamageBox = ttk.Checkbutton(
    MainFrame, text="Total Damage Delt", variable=TotalDamage)
VisionScoreBox = ttk.Checkbutton(
    MainFrame, text="Vision Score", variable=VisionScore)
SummonerSpellsBox = ttk.Checkbutton(
    MainFrame, text="Summoner Spells", variable=SummonerSpells)
CreepScoreBox = ttk.Checkbutton(
    MainFrame, text="Creep Score", variable=CreepScore)
ItemsBox = ttk.Checkbutton(MainFrame, text="Items", variable=Items)
GameResultBox = ttk.Checkbutton(MainFrame,text="Game Result (Win or Lose)",variable=GameResult)

# Submit button
SubmitButton = ttk.Button(MainFrame, text="Submit", command=Run)

# Player Name and Region input positions
PlayerNameLabel.grid(column=1, row=1, pady=5)
PlayerNameEntry.grid(column=2, row=1)
RegionLabel.grid(column=1, row=2, pady=5)
RegionComboBox.grid(column=2, row=2,)

# CallValues Checkboxes and Label positions
CallValuesLabel.grid(column=1, row=3, columnspan=3)
SummonerNameBox.grid(column=1, row=4, pady=2)
ChampionNameBox.grid(column=2, row=4, pady=2,)
KDABox.grid(column=3, row=4, pady=2,)
RollBox.grid(column=1, row=5, pady=2,)
LevelBox.grid(column=2, row=5, pady=2,)
RunesBox.grid(column=3, row=5, pady=2,)
TotalDamageBox.grid(column=1, row=6, pady=2,)
VisionScoreBox.grid(column=2, row=6, pady=2,)
SummonerSpellsBox.grid(column=3, row=6, pady=2,)
CreepScoreBox.grid(column=1, row=7, pady=2,)
ItemsBox.grid(column=2, row=7, pady=2,)
GameResultBox.grid(column=3, row=7, pady=2,)


# Submit button position
SubmitButton.grid(column=1, row=8, pady=2, columnspan=3)


# Running the Window
MainWin.mainloop()

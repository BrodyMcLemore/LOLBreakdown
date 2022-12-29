from tkinter import *
from tkinter import ttk, messagebox
from Project_Files.Func import OutputGames, SaveBook
from openpyxl import Workbook
from riotwatcher import LolWatcher
from Project_Files.config import API_KEY
from Project_Files.DictCalls import GetCurrentVersion


# Top Level Window handling
# Making the Window
MainWin = Tk()
MainWin.title("LOL Breakdown")
MainWin.resizable(width=False, height=False)
MainWin.geometry("300x200")
MainWin.iconbitmap("Project_Files\Mascot.ico")

# Handling the Frame
MainFrame = Frame(MainWin)
MainFrame.pack(padx=10, pady=10)
MainFrame.grid(column=0, row=0, sticky="NW")

# Setting Global Variables
# App Variables
PlayerName = StringVar()
RegionVal = StringVar()
SummonerName = IntVar(value=0)

# Working Variables
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
CallValues = ["inventory","summonerSpells"]
GameCount = 0
Row = 1
watcher = LolWatcher(API_KEY)


# Functions and Backend
def Run():
    Region = RegionServer[RegionVal.get()]
    AccountName = PlayerName.get()
    AccountInfo = watcher.summoner.by_name(Region, AccountName)
    MatchList = watcher.match.matchlist_by_puuid(Region, AccountInfo["puuid"])
    wb = Workbook()
    OutputGames(Region, MatchList, GameCount, Row, CallValues, watcher, wb,AccountName,GetCurrentVersion())
    if SaveBook(wb, AccountName) == "Success":
        messagebox.showinfo(
            "Success", "Your Game Data has been saved to a new folder named 'Output'.")
    elif SaveBook(wb, AccountName) == "Fail":
        messagebox.showerror(
            "Failure", "Your Game Data did NOT save correctly, please try again.")


# Building the Front End
# Player Name and Region Labels and Entries
PlayerNameLabel = ttk.Label(MainFrame, text="Player Name:", font=(
    'calibre', 12, 'bold'), anchor="center",takefocus=True)
RegionLabel = ttk.Label(MainFrame, text="Region:", font=(
    'calibre', 12, 'bold'), justify="left", anchor="center")
PlayerNameEntry = ttk.Entry(
    MainFrame, textvariable=PlayerName, font=('calibre', 10, 'normal'))
RegionComboBox = ttk.Combobox(MainFrame, textvariable=RegionVal,
                              values=RegionCommon, state="readonly", font=('calibre', 10, 'normal'))

# CallValue Checkboxes and Label
# List of call values: Summoner Name, Champion, Runes, Summoner spells, KDA (Just kills), damagedelt, vision score (wards?), CS, Items, role, level
CallValuesLabel = ttk.Label(MainFrame,text="Reported Values",font=(
    'calibre', 12, 'bold'), anchor="center")
SummonerNameBox = ttk.Checkbutton(MainFrame,text="Summoner Name",variable=SummonerName)


# Submit button
SubmitButton = ttk.Button(MainFrame, text="Submit", command=Run)

# Player Name and Region input positions 
PlayerNameLabel.grid(column=1, row=1, pady=5)
PlayerNameEntry.grid(column=2, row=1)
RegionLabel.grid(column=1, row=2, pady=5)
RegionComboBox.grid(column=2, row=2,)

# CallValues Checkboxes and Label positions 
CallValuesLabel.grid(column=1,row=3,columnspan=3)
SummonerNameBox.grid(column=1,row=4)

# Submit button position
SubmitButton.grid(column=1, row=5, pady=5, columnspan=2)

# Setting the Default value for Widgets
RegionComboBox.set("North America")


# Running the Window
MainWin.mainloop()

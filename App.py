from tkinter import *
from tkinter import ttk, messagebox
from Project_Files.Func import OutputGames, SaveBook
from openpyxl import Workbook
from riotwatcher import LolWatcher
from Project_Files.config import API_KEY


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
CallValues = ["summonerName", "championName", "teamPosition",
              "kills", "totalDamageDealt", "goldEarned", "visionScore", "win"]
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
    OutputGames(Region, MatchList, GameCount, Row, CallValues, watcher, wb)
    if SaveBook(wb, AccountName) == "Success":
        messagebox.showinfo(
            "Success", "Your Game Data has been saved to a new folder named 'Output'.")
    elif SaveBook(wb, AccountName) == "Fail":
        messagebox.showerror(
            "Failure", "Your Game Data did NOT save correctly, please try again")


# Building the Front End
# Labels, Input boxes, and Submit Buttons
PlayerNameLabel = ttk.Label(MainFrame, text="Player Name:", font=(
    'calibre', 10, 'bold'), anchor="center")
RegionLabel = ttk.Label(MainFrame, text="Region:", font=(
    'calibre', 10, 'bold'), justify="left", anchor="center")
PlayerNameEntry = ttk.Entry(
    MainFrame, textvariable=PlayerName, font=('calibre', 10, 'normal'))
RegionComboBox = ttk.Combobox(MainFrame, textvariable=RegionVal,
                              values=RegionCommon, state="readonly", font=('calibre', 10, 'normal'))
SubmitButton = ttk.Button(MainFrame, text="Submit", command=Run)

# Widget Positions
PlayerNameLabel.grid(column=1, row=2, pady=5)
PlayerNameEntry.grid(column=2, row=2)
RegionLabel.grid(column=1, row=3, pady=5)
RegionComboBox.grid(column=2, row=3,)
SubmitButton.grid(column=1, row=4, pady=5, columnspan=2)

# Setting the Default value for the RegionComboBox to "North America (na)"
RegionComboBox.set("North America")


# Running the Window
MainWin.mainloop()

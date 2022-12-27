from tkinter import *
from tkinter import ttk

## Top Level Window handling
# Making the Window
MainWin = Tk()
MainWin.title("LOL Breakdown")
MainWin.resizable(width=False,height=False)
MainWin.geometry("300x200")
MainWin.iconbitmap("Project_Files\Mascot.ico")

# Handling the Frame 
MainFrame = Frame(MainWin)
MainFrame.pack(padx=10,pady=10)
MainFrame.grid(column=0,row=0,sticky="NW")

## Setting Global Variables 
PlayerName = StringVar()
Region = StringVar()



## Functions and Backend
# Backend test
def TestPrint():
    print("Player Name is: " + PlayerName.get())
    print("The Region is: " + Region.get())

    PlayerName.set("")
    RegionComboBox.set("North American (na)")



## Building the Front End 
# Labels, Input boxes, and Submit Buttons
PlayerNameLabel = ttk.Label(MainFrame, text = "Player Name:", font=('calibre',10, 'bold'),anchor="center")
RegionLabel = ttk.Label(MainFrame, text = "Region:", font=('calibre',10, 'bold'),justify="left",anchor="center")
PlayerNameEntry = ttk.Entry(MainFrame, textvariable=PlayerName,font=('calibre',10,'normal'))
RegionComboBox = ttk.Combobox(MainFrame,textvariable=Region,values=["1","2","3"],state="readonly",font=('calibre',10,'normal'))
SubmitButton = ttk.Button(MainFrame,text="Submit",command=TestPrint)

# Widget Positions
PlayerNameLabel.grid(column=1,row=2,pady=5)
PlayerNameEntry.grid(column=2,row=2)
RegionLabel.grid(column=1,row=3,pady=5)
RegionComboBox.grid(column=2,row=3,)
SubmitButton.grid(column=1,row=4,pady=5,columnspan=2)

# Setting the Default value for the RegionComboBox to "North America (na)"
RegionComboBox.set("North American (na)")


## Running the Window
MainWin.mainloop()

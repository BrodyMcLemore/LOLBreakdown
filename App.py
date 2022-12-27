from tkinter import *
from tkinter import ttk

## Top Level Window handling
main = Tk()
main.grid()
main.title("LOL Breakdown")
main.geometry("300x200")


## Setting Global Variables 
PlayerName = StringVar()
Region = StringVar()



## Functions and Backend
def TestPrint():
    print("Player Name is: " + PlayerName.get())
    print("The Region is: " + Region.get())

    PlayerName.set("")
    RegionComboBox.set("North American (na)")



## Building the Front End 
# Labels, Input boxes, and Submit Buttons
PlayerNameLabel = ttk.Label(main, text = "Player Name:", font=('calibre',10, 'bold'))
RegionLabel = ttk.Label(main, text = "Region:", font=('calibre',10, 'bold'),justify="left")
PlayerNameEntry = ttk.Entry(main, textvariable=PlayerName,font=('calibre',10,'normal'))
RegionComboBox = ttk.Combobox(main,textvariable=Region,values=["1","2","3"],state="readonly",font=('calibre',10,'normal'))
SubmitButton = ttk.Button(main,text="Submit",command=TestPrint)

# Widget Positions
PlayerNameLabel.grid(column=1,row=1,pady=5)
RegionLabel.grid(column=1,row=2,pady=5)
PlayerNameEntry.grid(column=2,row=1)
RegionComboBox.grid(column=2,row=2)
SubmitButton.grid(column=1,row=3,pady=5)

# Setting the Default value for the RegionComboBox to "North America (na)"
RegionComboBox.set("North American (na)")




main.mainloop()

from tkinter import *
from tkinter import ttk

main = Tk()

MainFrame = ttk.Frame(main,padding=40,takefocus=True)
MainFrame.grid()

ttk.Label(MainFrame,text="I am a lable").grid(column=1,row=1)
ttk.Button(MainFrame,text="I am a Button").grid(column=1,row=2)
ttk.Checkbutton(MainFrame,text="I am a CheckButton").grid(column=1,row=3)
ttk.Combobox(MainFrame,values="I_am_a_ComboBox").grid(column=1,row=4)
ttk.Entry(MainFrame).grid(column=1,row=5)
ttk.Frame(MainFrame).grid(column=1,row=6)
ttk.Menubutton(MainFrame,text="I am a MenuButton").grid(column=1,row=7)
ttk.Notebook(MainFrame).grid(column=1,row=8)





main.mainloop()
# importing the main tkinter module and the ttk.
# always import both
from tkinter import *
from tkinter import ttk

# This line assigns the name of the window, and is the reference going forward
app = Tk()

# this creates the frame inside of the apps and mangages the widgets inside
Frame = ttk.Frame(app, padding=10)

# This assigns a grid ot the window and allows things to be placed on it based on cords 
Frame.grid()

# This is adding a button and a label to the frame
# A label is text on the screen that is used to identify another object
ttk.Label(Frame, text="Hello World!").grid(column=0, row=0)
# A button is an interactive object that can apply a command or func call
ttk.Button(Frame, text="Quit", command=app.destroy).grid(column=1, row=0)

# Calling the app to run
app.mainloop()
from ProjectFiles.BoilerPlate import *
from openpyxl import Workbook
import os

WorkBook = Workbook()

HeaderList = ["Combat","Damage Dealt","Damage Taken and Healed","Vision","Income & Items","Minons","Misc"]

for i in range(0,5):
    MakeSheets(WorkBook,str(i))
    row = 3
    for header in range(len(HeaderList)):
        #MakeHeader(Title,Row,Lenght,WorkSheet)
        MakeHeader(HeaderList[header],row,4,WorkBook[str(i)])
        row += 3


del WorkBook["Sheet"]

WorkBook.save("Test.xlsx")

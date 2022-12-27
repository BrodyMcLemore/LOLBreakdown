from ProjectFiles.BoilerPlate import *
from openpyxl import Workbook
import os

WorkBook = Workbook()

for i in range(0,5):
    MakeSheets(WorkBook,str(i))

del WorkBook["Sheet"]
WorkBook.save(str(os.getcwd())+"Test.xlsx")

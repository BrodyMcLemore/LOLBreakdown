from riotwatcher import LolWatcher
from datetime import datetime
import time
import os

Key = open("Key.txt","r")
Key = Key.read().rstrip("\n")

MyKey = Key
#MyReg = input("What is your region?: ")
MyReg = "na1"
watcher = LolWatcher(MyKey)
#AccountName = input("What is your Account Name?: ")
AccountName = "ChaoticThunder0"
try:
    MyAccount = watcher.summoner.by_name(MyReg, AccountName)
except:
    print("Either your Region and/or Account Name is worng. Please try again.")
    exit()
MyMatches = watcher.match.matchlist_by_puuid(MyReg, MyAccount["puuid"])

for i in range(len(MyMatches)):
    MatchDetail = watcher.match.by_id(MyReg,MyMatches[i])
    if MatchDetail["info"]["gameMode"] == "CLASSIC":
        for x in range(5):
            if MatchDetail["info"]["participants"][x]["teamPosition"] != "UTILITY":
                print(MatchDetail["info"]["participants"][x]["championName"] + " "+ MatchDetail["info"]["participants"][x]["teamPosition"])
            else:
                print(MatchDetail["info"]["participants"][x]["championName"] + " " + "Support")
        print("-------")

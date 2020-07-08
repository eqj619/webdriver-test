# Scrapping Japanese tennis player ranking from ATP web site
# Copyright 2020 Eiji Oga @ Suo Solutions
#
# exvironment:
#   mac os 10.15
#   python 3.7.7

from selenium import webdriver
import time
import datetime
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as req
import json
import requests
import re

def cleanUpTag(listTag):
    if type(listTag.string) != type(None):
        return(listTag.string.replace("\n","").replace("\t", ""))
    else:
        return("")

#===
print("Date, Ranking, Move, Player, Age, Points, Tourn Played, Points Dropping, Next Best")

browser = webdriver.Chrome()
browser.implicitly_wait(3)

now = datetime.datetime.now()
timestamp=now.strftime("%Y-%m-%d")

# get rank date lisf from pulldown menu in ATP website
atpUrl = "https://www.atptour.com/en/rankings/singles"
browser.get(atpUrl)
time.sleep(3)

pagehtml = browser.page_source
soup = BeautifulSoup(pagehtml, 'html.parser')
rankdates = soup.find_all('li')

rankDataList = []
count = 0
for tmp in rankdates:
        if type(tmp.string) != type(None):
            rankdate = tmp.string.replace("\n","").replace("\t", "")
            if len(rankdate) == 10: # reject other pulldown menu
                if rankdate[0] == '1' or rankdate[0] == '2':
                    if count != 0:  # skip default pulldown value
                        #print(rankdate.replace(".","-"))
                        rankDataList.append(rankdate.replace(".","-"))
                    count += 1


# Retrieve ranking history at Japanese player
listRank  =[]
listMove = []
listPlayer = []
listAge = []
listPoints = []
listTourn = []
listPts = []
listNext = []

for tag in rankDataList:
    atpUrl = "https://www.atptour.com/en/rankings/singles?rankDate=" + tag + "&rankRange=1-1000&countryCode=JPN"
    browser.get(atpUrl)
    time.sleep(1)

    pagehtml = browser.page_source
    soup = BeautifulSoup(pagehtml, 'html.parser')
    listRank = soup.find_all(class_ = 'rank-cell')
    listMove = soup.find_all(class_ = 'move-cell')
    listPlayer = soup.find_all(class_ = 'player-cell')
    listAge = soup.find_all(class_ = 'age-cell')
    listPoints = soup.find_all(class_ = 'points-cell')
    listTourn = soup.find_all(class_ = 'tourn-cell')
    listPts = soup.find_all(class_ = 'pts-cell')
    listNext = soup.find_all(class_ = 'next-cell')

    #for tmp in listPlayer:
    #    print(tmp.find('a').string)
    for i in range(len(listRank)):
        s = cleanUpTag(listPlayer[i].find('a'))
        ss = cleanUpTag(listPoints[i].find('a'))
        sss = cleanUpTag(listTourn[i].find('a'))
        print(tag + ", ",
            cleanUpTag(listRank[i])+ ", ",
            cleanUpTag(listMove[i]) + ", ",
            re.sub(r"^\s+", "", s)  + ", ",
            cleanUpTag(listAge[i])  + ", ",
            ss.replace(",","") + ", ",
            sss + ", ",
            cleanUpTag(listPts[i])  + ", ",
            cleanUpTag(listNext[i])
            )
    time.sleep(1)

time.sleep(3)
browser.close()

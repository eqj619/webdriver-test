from selenium import webdriver
import time
import datetime
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as req
import json
import requests

#===
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
            if len(rankdate) == 10:
                if rankdate[0] == '1' or rankdate[0] == '2':
                    if count != 0:
                        #print(rankdate.replace(".","-"))
                        rankDataList.append(rankdate.replace(".","-"))
                    count += 1


# Retrieve ranking history at Japanese player
for tag in rankDataList:
    atpUrl = "https://www.atptour.com/en/rankings/singles?rankDate=" + tag + "&rankRange=1-5000&countryCode=JPN"
    browser.get(atpUrl)
    time.sleep(1)

'''
rankDateList = []
rankDateList = soup.find_all('li', text = 'date-value')
print(len(rankDateList))
'''

'''
start_dt = datetime.datetime.strptime(start_dt, '%Y%m%d')
#start_dt = (start_dt - datetime.timedelta(days=50)).strftime('%Y-%m-%d')
for i in reversed(range(0, 50)):
    dt = (start_dt - datetime.timedelta(days=i*7)).strftime('%Y-%m-%d')
    print(dt)

    #url = "https://sa.www4.irs.gov/irfof-wmsp/login"
    atpUrl = "https://www.atptour.com/en/rankings/singles?rankDate=" + dt + "&rankRange=1-5000&countryCode=JPN"
    browser.get(atpUrl)
    time.sleep(3)

    submit_button = browser.find_element_by_id('filterSubmit')
    submit_button.click()
    time.sleep(3)

https://www.atptour.com/en/rankings/singles?rankDate=2020-03-16&rankRange=1-5000&countryCode=JPN
<button id="filterSubmit" data-resulturl="/en/rankings/singles" data-urltype="path" class="filter-submit">
            Go
        </button>
'''

'''
# print the status of pandemic support check
pagehtml = browser.page_source
soup = BeautifulSoup(pagehtml, 'html.parser')

now = datetime.datetime.now()
timestamp=now.strftime("%D %T")
print(timestamp + '\t' + soup.find(class_ = 'login-title').string)
'''

time.sleep(3)
browser.close()

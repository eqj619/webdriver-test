# pip install selenium
# brew cask install chromedriver
from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.implicitly_wait(3)

url = "https://sa.www4.irs.gov/irfof-wmsp/notice"
browser.get(url)
time.sleep(3)

submit_button = browser.find_element_by_name('submit')
submit_button.click()
time.sleep(1)

#input SSN
ssn_area = browser.find_element_by_id('ssnInput')
ssn_area.send_keys("111223333")
time.sleep(1)

#input DOB mm/dd/yyyy
dob_area = browser.find_element_by_id('dobInput')
dob_area.send_keys("mm/dd/yyyy")
time.sleep(1)

#input address1 street and number
address_area = browser.find_element_by_id('addressInput')
address_area.send_keys("12345 sss bbb")
time.sleep(1)

#input zip code
zip_area = browser.find_element_by_id('zipCodeInput')
zip_area.send_keys("12345")
time.sleep(1)

#see status of pandemic support check
submit_button = browser.find_element_by_name('submit')
submit_button.click()
time.sleep(3)

pagehtml = browser.page_source
soup = BeautifulSoup(pagehtml, 'html.parser')
now = datetime.datetime.now()
timestamp=now.strftime("%D %T")
print(timestamp + '\t' + soup.find(class_ = 'login-title').string)
#time.sleep(3)
#browser.close()

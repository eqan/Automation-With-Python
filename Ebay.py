import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

search_item = input("Enter Item: ")
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", desired_capabilities=capabilities)

try:
    driver.get(r'https://www.ebay.com/')
    driver.implicitly_wait(30)
    
    loginBox = driver.find_element_by_xpath('//*[@id="gh-ac"]')
    loginBox.send_keys(search_item)
 
    nextButton = driver.find_elements_by_xpath('//*[@id="gh-btn"]')
    nextButton[0].click()

    try:
        nextButton = driver.find_elements_by_xpath('//*[@class="fake-menu-button srp-controls__control"]')
        nextButton[0].click()
        nextButton = driver.find_elements_by_xpath('//*[@_sp="p2351460.m4116.l5869.c4"]')
        nextButton[0].click()
    except Exception as inst:
        print(inst)

    time.sleep(100)
    print('Search Successful')
except Exception as inst:
    print(inst)

driver.close()

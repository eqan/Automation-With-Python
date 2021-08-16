import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
search_item = input("Enter Item: ")
model = input("Enter Model: ")
free_shipping = int(input("Press 1 for free shipping: "))
condition = input("Enter Condition: ")
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(options=chrome_options, executable_path="C:\chromedriver.exe", desired_capabilities=capabilities)

try:
    driver.get(r'https://www.ebay.com/')
    driver.implicitly_wait(30)
    
    searchItemBox = driver.find_element_by_xpath('//*[@id="gh-ac"]')
    searchItemBox.send_keys(search_item)
    searchItemBox.submit()

    temp_options_list=[]
    options_list=[]
    temp_options_list = driver.find_elements_by_xpath('//*[@class="srp-related-searches"]//a[@href]')
    for option in temp_options_list:
        options_list.append(option.get_attribute('href'))
    link=""
    for i, option in enumerate(options_list):
        x=re.search(model + "&.*", option)
        if(x):
            link=option
            break
    #     for windows change command to control. 
    if(link == ""):
        print("Search Query Not Found!\n")
        exit(1)
    else:
        #     for windows change command to control. 
        print(link)
        driver.execute_script('''window.open("' +'''+ link +'''", "_blank");''')

    time.sleep(5)

    #get current window handle
    p = driver.current_window_handle

    #get first child window
    chwd = driver.window_handles

    for w in chwd:
        if(w!=p):
            driver.switch_to.window(w)
            break

    try:
        nextButton = driver.find_elements_by_xpath('//*[@class="fake-menu-button srp-controls__control"]')
        nextButton[0].click()
        nextButton = driver.find_elements_by_xpath('//*[@_sp="p2351460.m4116.l5869.c4"]')
        nextButton[0].click()
        if(free_shipping == 1):
            nextButton = driver.find_elements_by_xpath('//*[text()="Shipping"]')
            nextButton[0].click()
            nextButton = driver.find_elements_by_xpath('//*[@_sp="p2351460.m44506.l50884.c1"]')
            nextButton[0].click()
        nextButton = driver.find_elements_by_xpath('//span[text()="Condition"]')
        nextButton[0].click()
        if(condition == "New"):
            nextButton = driver.find_elements_by_xpath('//*[@_sp="p2351460.m44506.l45851.c2"]')
            nextButton[0].click()
        elif(condition == "Open Box"):
            nextButton = driver.find_elements_by_xpath('//*[@_sp="p2351460.m44506.l45851.c3"]')
            nextButton[0].click()
        elif(condition == "Refurbrished"):
            nextButton = driver.find_elements_by_xpath('//*[@_sp="p2351460.m44506.l45851.c4"]')
            nextButton[0].click()
        elif(condition == "Used"):
            nextButton = driver.find_elements_by_xpath('//*[@_sp="p2351460.m44506.l45851.c5"]')
            nextButton[0].click()
        elif(condition == "Parts"):
            nextButton = driver.find_elements_by_xpath('//*[@_sp="p2351460.m44506.l45851.c6"]')
            nextButton[0].click()
        elif(condition == "Any"):
            nextButton = driver.find_elements_by_xpath('//*[@_sp="p2351460.m44506.l45851.c1"]')
            nextButton[0].click()
        else:
            print("Invalid Option\n")

    except Exception as inst:
        print(inst)

    for w in chwd:
        if(p!=w):
            driver.switch_to.window(p)
            break

    nextButton = driver.find_elements_by_xpath('//*[@class="fake-menu-button srp-controls__control"]')
    nextButton[0].click()

    time.sleep(100)

    print('Search Successful')
except Exception as inst:
    print(inst)

driver.close()

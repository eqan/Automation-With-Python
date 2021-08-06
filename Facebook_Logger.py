import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
from getpass import getpass
  
facebook_id = input('Enter Email: ')
password = getpass('Enter Password: ')
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", desired_capabilities=capabilities)

try:
    driver.get(r'https://www.facebook.com/')
    driver.implicitly_wait(30)

    loginBox = driver.find_element_by_xpath('//*[@name ="email"]')
    loginBox.send_keys(facebook_id)

    passWordBox = driver.find_element_by_xpath('//*[@id ="pass"]')
    passWordBox.send_keys(password)

    nextButton = driver.find_elements_by_xpath('//*[@data-testid="open-registration-form-button"]')
    nextButton[0].click()
    
    driver.implicitly_wait(5)
    print('Login Successful!')
except Exception as inst:
    print(inst)
    
driver.close()

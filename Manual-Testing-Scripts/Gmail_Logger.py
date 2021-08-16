import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
from getpass import getpass
  
gmail_id = input('Enter Email: ')
password = getpass('Enter Password: ')
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", desired_capabilities=capabilities)

try:
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
    'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
    '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    driver.implicitly_wait(30)

    loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
    loginBox.send_keys(gmail_id)

    nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
    nextButton[0].click()

    passWordBox = driver.find_element_by_xpath('//*[@id ="password"]')
    passWordBox.send_keys(password)

    nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
    nextButton[0].click()
    
    print('Login Successful!')
except Exception as inst:
    print(inst)
    
driver.close()

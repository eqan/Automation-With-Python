import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
import time

firefox_options = Options()
firefox_options.add_argument("--start-maximized")
driver = webdriver.Firefox(executable_path=r'C:\Users\Eqan Ahmad\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe', options=firefox_options)
driver.get(r'https://docs.google.com/forms/d/e/1FAIpQLSfG5FoKgxAfQ2zSILgAdvYKZjgpQkcaDXI0CkpNWpgEp6xnow/viewform')

def page1():
    time.sleep(3)
    driver.find_element_by_xpath('//*[@class="quantumWizTextinputPaperinputInput exportInput"]').send_keys("Eqan Ahmad")
    driver.find_element_by_xpath('//*[@class="appsMaterialWizButtonPaperbuttonContent exportButtonContent"]').click()

def page2():
    driver.find_element_by_xpath('//*[@class="quantumWizTextinputPaperinputInput exportInput"]').send_keys("19")
    driver.find_element_by_xpath('//*[text()="Next"]').click()

def page3():
    driver.find_element_by_xpath('//*[@class="quantumWizTextinputPaperinputInput exportInput"]').send_keys("19F0256")
    driver.find_element_by_xpath('//*[text()="Next"]').click()

def page4():
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="i6"]').click()
    driver.find_element_by_xpath('//*[@id="i9"]').click()
    driver.find_element_by_xpath('//*[@id="i12"]').click()
    driver.find_element_by_xpath('//*[text()="Next"]').click()

def page5():
    try:
        time.sleep(2)
        driver.find_element_by_xpath('//*[text()="Choose"]').click()
        time.sleep(2)
        driver.find_elements_by_xpath('//*[text()="DB"]')[1].click()
    except Exception as inst:
        print("Couldn't select the options")
    webElement = driver.find_element_by_xpath(By.XPATH('//*[@class="appsMaterialWizButtonPaperbuttonContent exportButtonContent"]'))
    webElement.sendKeys(Keys.TAB)
    webElement.sendKeys(Keys.ENTR);

def close_connection():
    driver.close()
    driver.quit()

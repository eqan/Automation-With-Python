import json
from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    
    @classmethod
    def SetUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.maximize_window()

    def test_site(self):
        gmail_id = "Admin"
        password = "admin123"
        try:
            self.driver.get(r'https://opensource-demo.orangehrmlive.com/')
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys(gmail_id)
            self.driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(password)
            self.driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
            self.driver.find_element_by_xpath('//*[@id="welcome"]').click()
            self.driver.find_element_by_xpath('//*[@text()="Logout"]').click()
            print('Login Successful!')
        except Exception as inst:
            print(inst)
        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')

if __name__ == "__main__":
    unittest.main()

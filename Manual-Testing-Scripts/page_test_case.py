import unittest
from selenium import webdriver
import LoginPage
import HomePage
import time

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.maximize_window()

    def test_site(self):
        gmail_id = "Admin"
        password = "admin123"
        driver = self.driver
        try:
            driver.get(r'https://opensource-demo.orangehrmlive.com/')
            driver.implicitly_wait(10)
            
            login = LoginPage(driver)
            login.enter_username(gmail_id)
            login.enter_username(password)
            login.click_login()

            homepage = HomePage(driver)
            homepage.welcome_click()
            homepage.logout_click()
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

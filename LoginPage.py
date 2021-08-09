import Locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(Locators.username_id).sendkeys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(Locators.password_id).sendkeys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_btn).click()

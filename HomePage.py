class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def welcome_click(self):
        self.driver.find_element_by_id(self.welcome_link).click()

    def logout_click(self):
        self.driver.find_element_by_id(self.logout_link).click()

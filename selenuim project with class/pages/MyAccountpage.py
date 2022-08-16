from selenium.webdriver.common.by import By
from pages.Main_page import *
from pages.Base_Page import *


class MyAccount_page(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)


    locators = {"home": (By.CLASS_NAME, "home")}

    def home(self):
        self._driver.find_element(*self.locators["home"]).click()
        return MainPage(self._driver)

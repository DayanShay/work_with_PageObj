from selenium.webdriver.common.by import By
from selenuim_project_with_class.pages.Base_Page import *


class MyAccount_page(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)
        self._title = 'My account - My Store'

    def home(self) -> "MainPage":
        """
        clicking on home button
        :return: MainPage:main page
        """
        from selenuim_project_with_class.pages.Main_page import MainPage

        self._driver.find_element(*self.locators["home"]).click()
        return MainPage(self._driver)

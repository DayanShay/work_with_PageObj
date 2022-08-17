from playwright_project_with_class.pages.Base_Page import *

class MyAccount_page(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)
        self._title = 'My account - My Store'

    def home(self):
        from playwright_project_with_class.pages.Main_page import MainPage
        self._driver.locator(self.locators["home"]).click()
        return MainPage(self._driver)

from selenium.webdriver.common.by import By
from selenuim_project_with_class.pages.Base_Page import BaseObj


class AuthenticationPage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)


    locators = {"email":(By.ID,"email"),
                "password":(By.ID,"passwd"),
                "home":(By.CLASS_NAME,"home"),
                "SubmitLogin":(By.ID,"SubmitLogin")}

    def login(self,email:str,password:str):
        self._driver.find_element(*self.locators["email"]).send_keys(email)
        self._driver.find_element(*self.locators["password"]).send_keys(password)
        self._driver.find_element(*self.locators["SubmitLogin"]).click()
        return AuthenticationPage(self._driver)

    def home(self):
        from pages.Main_page import MainPage
        self._driver.find_element(*self.locators["home"]).click()
        return MainPage(self._driver)

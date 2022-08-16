from selenium.webdriver.common.by import By
from selenuim_project_with_class.pages.Base_Page import BaseObj
from selenium.webdriver.support import expected_conditions as EC
from selenuim_project_with_class.pages.MyAccountpage import MyAccount_page

class AuthenticationPage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)


    locators = {"email":(By.ID,"email"),
                "password":(By.ID,"passwd"),
                "home":(By.CLASS_NAME,"home"),
                "SubmitLogin":(By.ID,"SubmitLogin"),
                "error_message_location": (By.CLASS_NAME, 'alert'),
                "error_text_message": (By.TAG_NAME, 'li')
                }

    def login(self,email:str,password:str):
        self._driver.find_element(*self.locators["email"]).send_keys(email)
        self._driver.find_element(*self.locators["password"]).send_keys(password)
        self._driver.find_element(*self.locators["SubmitLogin"]).click()
        return MyAccount_page(self._driver)

    def home(self):
        from selenuim_project_with_class.pages.Main_page import MainPage
        self._driver.find_element(*self.locators["home"]).click()
        return MainPage(self._driver)

    def get_error_msg(self):
        error_message_location = self.wait.until(EC.presence_of_element_located(self.locators["error_message_location"]))
        error_text_message = error_message_location.find_element(*self.locators["error_text_message"]).text
        return error_text_message

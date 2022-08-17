import time
from selenium.webdriver.common.by import By
from playwright_project_with_class.pages.Base_Page import BaseObj
from selenium.webdriver.support import expected_conditions as EC
from playwright_project_with_class.pages.MyAccountpage import MyAccount_page

class AuthenticationPage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)


    locators = {"email":'id=email',
                "password":'id=passwd',
                "home":(By.CLASS_NAME,"home"),
                "SubmitLogin":'id=SubmitLogin',
                "error_message_location": '.alert'
                }

    def login(self,email:str,password:str):
        self._driver.locator(self.locators["email"]).fill(email)
        self._driver.locator(self.locators["password"]).fill(password)
        self._driver.locator(self.locators["SubmitLogin"]).click()
        return MyAccount_page(self._driver)

    def home(self):
        from playwright_project_with_class.pages.Main_page import MainPage
        self._driver.find_element(*self.locators["home"]).click()
        return MainPage(self._driver)

    def get_error_msg(self):
        time.sleep(1)
        error_message_location = self._driver.locator(self.locators["error_message_location"]).all_text_contents()
        error_message_location = error_message_location[0].strip()
        # changing the way the text gets to error_text_message - strip - split - replace - >  'There is X error\n\t\t\n\t\t\t\tERRORMSG.'
        error_text_message = error_message_location.replace('\t',"").replace('\n\n',"\n").split('\n')
        return error_text_message



import time
from selenium.webdriver.common.by import By
from playwright_project_with_class.pages.Base_Page import BaseObj
from playwright_project_with_class.pages.MyAccountpage import MyAccount_page


class ForgetPasswordPage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)
        self._title = 'Forgot your password - My Store'



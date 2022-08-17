from selenuim_project_with_class.pages.Base_Page import BaseObj
from selenium.webdriver.support import expected_conditions as EC
from selenuim_project_with_class.pages.MyAccountpage import MyAccount_page
from selenuim_project_with_class.pages.forget_password_page import ForgetPasswordPage


class AuthenticationPage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email: str, password: str) -> MyAccount_page:
        """
        Make Login on page
        :param email: str : email need to fill in
        :param password: str: password need to fill in
        :return: MyAccount_page:
        """
        self._driver.find_element(*self.locators["email"]).send_keys(email)
        self._driver.find_element(*self.locators["password"]).send_keys(password)
        self._driver.find_element(*self.locators["SubmitLogin"]).click()
        return MyAccount_page(self._driver)

    def home(self) -> "MainPage":
        """
        Click on Home button on the page
        :return: MainPage:
        """
        from selenuim_project_with_class.pages.Main_page import MainPage
        self._driver.find_element(*self.locators["home"]).click()
        return MainPage(self._driver)

    def get_error_msg(self) -> str:
        """
        gets the error msg on login filed
        :return: str: msg of the failed error
        """
        error_message_location = self.wait.until(
            EC.presence_of_element_located(self.locators["error_message_location"]))
        error_text_message = error_message_location.find_element(*self.locators["error_text_message"]).text
        return error_text_message

    def forget_password(self) -> ForgetPasswordPage:
        """
        click on forget password button on login section
        :return: ForgetPasswordPage:
        """
        self.wait.until(EC.element_to_be_clickable(self.locators["forgot_password"])).click()
        return ForgetPasswordPage(self._driver)

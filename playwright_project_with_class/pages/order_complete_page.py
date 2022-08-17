from selenium.webdriver.common.by import By
from playwright_project_with_class.pages.Base_Page import BaseObj
from selenium.webdriver.support import expected_conditions as EC


class Order_complete_Page(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)
        self._order_msg_templet = 'Your order on My Store is complete.'


    def get_confirm_msg(self):
        msg_location = self._driver.locator(".cheque-indent").text_content()
        msg_text = msg_location.replace('\n', "").replace('\t', "")
        return msg_text

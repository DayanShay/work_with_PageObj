from selenium.webdriver.common.by import By
from playwright_project_with_PageObj.PageObjs.Base_Page import BaseObj
from selenium.webdriver.support import expected_conditions as EC


class Order_complete_Page(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)
        self._order_msg_templet = 'Your order on My Store is complete.'
    locators = {
                "msg_confirm": ".cheque-indent"
                }
    def get_confirm_msg(self) -> str:
        """
        get the confirm order msg
        :return: str : order confirm msg
        """
        msg_location = self._driver.locator(self.locators["msg_confirm"]).text_content()
        msg_text = msg_location.replace('\n', "").replace('\t', "")
        return msg_text

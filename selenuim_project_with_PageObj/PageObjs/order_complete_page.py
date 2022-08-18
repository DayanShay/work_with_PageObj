from selenium.webdriver.common.by import By
from selenuim_project_with_PageObj.PageObjs.Base_Page import BaseObj
from selenium.webdriver.support import expected_conditions as EC


class Order_complete_Page(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)
        self._order_msg_templet = 'Your order on My Store is complete.'

    def get_confirm_msg(self) -> str:
        """
        get the confirm order msg
        :return: str : order confirm msg
        """
        msg_location = self.wait.until(EC.presence_of_element_located(self.locators["msg_confirm"]))
        msg_text = msg_location.text
        return msg_text

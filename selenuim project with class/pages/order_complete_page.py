from selenium.webdriver.common.by import By
from pages.Base_Page import BaseObj
from selenium.webdriver.support import expected_conditions as EC

class Order_complete_Page(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)
        self._order_msg_templet = 'Your order on My Store is complete.'

    locators = {"msg_confirm": (By.CLASS_NAME, "cheque-indent")
                }
    def get_confirm_msg(self):
        msg_location = self.wait.until(EC.presence_of_element_located(self.locators["msg_confirm"]))
        msg_text = msg_location.text
        return msg_text

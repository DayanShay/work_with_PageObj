from selenium.webdriver.common.by import By
from playwright_project_with_class.pages.order_complete_page import Order_complete_Page
from playwright_project_with_class.pages.Base_Page import BaseObj
from selenium.webdriver.support import expected_conditions as EC



class Orderpage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {"proceed_checkout_buttons": (By.CLASS_NAME, "cart_navigation"),
                "proceed_checkout": (By.CLASS_NAME, "button"),
                "ship_check_box": (By.ID,"uniform-cgv"),
                "bank_wire_check": (By.CLASS_NAME,"bankwire"),
                "order_button_location": (By.ID, "cart_navigation"),
                "i_confirm_button": (By.TAG_NAME, "button")
                }

    def complete_order(self):
        # start by - click - proceed.
        self.click_proceed_to_checkout_order()
        # 2 - click - proceed.
        self.click_proceed_to_checkout_order()
        # 3 - click - on ship and proceed.
        self.check_ship_box_and_proceed_to_checkout()
        # 4 - click on wire option
        self.check_on_bank_wire()
        # 5 - click i confirm order
        self.check_i_confirm_order()

        # 6 - return the driver as Confirm order page
        return Order_complete_Page(self._driver)

    def click_proceed_to_checkout_order(self):
        proceed_checkout_buttons = self.wait.until(EC.presence_of_element_located(self.locators["proceed_checkout_buttons"]))
        proceed_checkout_buttons.find_element(*self.locators["proceed_checkout"]).click()


    def check_ship_box_and_proceed_to_checkout(self):
        proceed_checkout = self._driver.find_element(*self.locators["ship_check_box"])
        proceed_checkout.click()
        self.click_proceed_to_checkout_order()

    def check_on_bank_wire(self):
        proceed_checkout = self._driver.find_element(*self.locators["bank_wire_check"])
        proceed_checkout.click()

    def check_i_confirm_order(self):
        order_button_location = self._driver.find_element(*self.locators["order_button_location"])
        i_confirm_button = order_button_location.find_element(*self.locators["i_confirm_button"])
        i_confirm_button.click()



import logging
from selenuim_project_with_class.pages.order_complete_page import Order_complete_Page
from selenuim_project_with_class.pages.Base_Page import BaseObj
from selenium.webdriver.support import expected_conditions as EC

MSG_info = logging.getLogger(__name__).info

class Orderpage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)

    def complete_order(self) -> Order_complete_Page:
        """
        doing all steps of order page at once
        :return:Order_complete_Page
        """
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

    def click_proceed_to_checkout_order(self) -> None:
        """
        click_proceed_to_checkout
        """
        proceed_checkout_buttons = self.wait.until(
            EC.presence_of_element_located(self.locators["proceed_checkout_buttons"]))
        proceed_checkout_buttons.find_element(*self.locators["proceed_checkout_order"]).click()
        MSG_info("Clicked on proceed to checkout")


    def check_ship_box_and_proceed_to_checkout(self) -> None:
        """
        check_ship_box_and_proceed_to_checkout
        """
        proceed_checkout = self._driver.find_element(*self.locators["ship_check_box"])
        proceed_checkout.click()
        MSG_info("Clicked on ship box")
        self.click_proceed_to_checkout_order()


    def check_on_bank_wire(self)-> None:
        """
        check_on_bank_wire
        """
        proceed_checkout = self._driver.find_element(*self.locators["bank_wire_check"])
        proceed_checkout.click()
        MSG_info("Clicked on bank wire method")

    def check_i_confirm_order(self) -> None:
        """
        check_i_confirm_order
        """
        order_button_location = self._driver.find_element(*self.locators["order_button_location"])
        i_confirm_button = order_button_location.find_element(*self.locators["i_confirm_button"])
        i_confirm_button.click()
        MSG_info("Clicked on i confirm order")


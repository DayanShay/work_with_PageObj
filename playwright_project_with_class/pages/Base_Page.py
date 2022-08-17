import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseObj:
    def __init__(self, driver):
        self._driver = driver

    locators = {"search_bar": "id=search_query_top",
                "submit_search": 'xpath=//*[@id="searchbox"]/button',
                "proceed_checkout": 'text=Proceed to checkout',
                "ship_check_box": 'id=cgv',
                "bank_wire_check": 'text=Pay by bank wire',
                "order_button_location": '.cart_navigation',
                "i_confirm_button": 'xpath=//*[@id="cart_navigation"]/button',
                "email": 'id=email',
                "password": 'id=passwd',
                "home": ".home",
                "SubmitLogin": 'id=SubmitLogin',
                "error_message_location": '.alert',"SignIn": ".login",
                "product_price": ".product-price",
                "product_container": ".product-container",
                "add_to_cart": '.ajax_add_to_cart_button',
                "msg_confirm": ".cheque-indent"
                }

    def search(self, search_ward: str):
        self._driver.locator(self.locators["search_bar"]).fill(search_ward)
        self._driver.locator(self.locators["submit_search"]).click()
        time.sleep(3)
        products_list = self._driver.query_selector_all(self.locators["product_container"])
        return products_list

    def get_title(self):
        return self._driver.title()

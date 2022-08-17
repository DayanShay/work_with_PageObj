import time

from selenium.webdriver.common.by import By
from playwright_project_with_class.pages.Authentication_page import AuthenticationPage
from playwright_project_with_class.pages.Base_Page import BaseObj
from playwright_project_with_class.pages.Order_page import Orderpage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {"SignIn": ".login",
                "search_bar": "id=search_query_top",
                "submit_search": 'xpath=//*[@id="searchbox"]/button',
                "search_res": (By.ID, "center_column"),
                "product_price": ".product-price",
                "product_container": ".product-container",
                "button_container": (By.CLASS_NAME, "button-container"),
                "add_to_cart": '.ajax_add_to_cart_button',
                "product_item": (By.TAG_NAME, "span"),
                "proceed_checkout": (By.LINK_TEXT, "Proceed to checkout")
                }

    def SignIn(self):
        self._driver.locator(self.locators["SignIn"]).click()
        return AuthenticationPage(self._driver)

    def find_cheap_from_search(self,product_containers):
        price_list = {}
        for product_container in product_containers:
            price = product_container.query_selector(self.locators["product_price"]).text_content().strip()
            price_list[price.strip()] = product_container
        cheapest_price = min(price_list.keys())
        cheapest_dress = price_list[cheapest_price]
        return cheapest_price,cheapest_dress

    def click_add_to_cart(self,dress):
        dress.click()
        add_button = dress.query_selector(self.locators["add_to_cart"])
        add_button.click()

    def click_proceed_to_checkout(self):
        self.wait.until(EC.presence_of_element_located(self.locators["proceed_checkout"])).click()
        # proceed_checkout = self._driver.find_element(*self.locators["proceed_checkout"])
        # proceed_checkout.click()
        return Orderpage(self._driver)


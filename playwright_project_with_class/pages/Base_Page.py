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
                "search_res": (By.ID, "center_column"),
                "product_container": ".product-container",
                "product_block": (By.CLASS_NAME, "right-block"),
                "product_details": (By.CLASS_NAME, "content_price"),
                "product_price": (By.TAG_NAME, "span")}

    def search(self, search_ward: str):
        self._driver.locator(self.locators["search_bar"]).fill(search_ward)
        self._driver.locator(self.locators["submit_search"]).click()
        time.sleep(3)
        products_list = self._driver.query_selector_all(self.locators["product_container"])
        return products_list

    def get_title(self):
        return self._driver.title()




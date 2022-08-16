from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class BaseObj:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 20)

    locators = {"search_bar": (By.ID, "search_query_top"),
                "submit_search": (By.NAME,"submit_search"),
                "search_res": (By.ID, "center_column"),
                "product_container": (By.CLASS_NAME, "product-container"),
                "product_block": (By.CLASS_NAME, "right-block"),
                "product_details": (By.CLASS_NAME, "content_price"),
                "product_price": (By.TAG_NAME, "span")}

    def search(self, search_ward: str):
        self._driver.find_element(*self.locators["search_bar"]).send_keys(search_ward)
        self.wait.until(EC.element_to_be_clickable(self.locators["submit_search"])).click()
        self.wait.until(EC.presence_of_element_located(self.locators["search_res"]))
        products_list = self._driver.find_elements(*self.locators["product_container"])
        return products_list





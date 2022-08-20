from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseObj:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 20)
        self._search_word = None

    base_locators = {"search_bar": (By.ID, "search_query_top"),
                     "submit_search": (By.NAME, "submit_search"),
                     "search_res": (By.ID, "center_column"),
                     "product_container": (By.CLASS_NAME, "product-container"),
                     }

    def search(self, search_word: str) -> [webdriver]:
        """
        go on top search bar and make a search of the search word
        :param search_word: str: the word need to search
        :return: [webdriver] : list of webdriver elements
        """
        self._driver.find_element(*self.base_locators["search_bar"]).send_keys(search_word)
        self.wait.until(EC.element_to_be_clickable(self.base_locators["submit_search"])).click()
        self.wait.until(EC.presence_of_element_located(self.base_locators["search_res"]))
        products_list = self._driver.find_elements(*self.base_locators["product_container"])
        self._search_word = search_word
        return products_list

    @property
    def title(self) -> str:
        """
        get the title of this page
        :return: str : page title
        """
        return self._driver.title

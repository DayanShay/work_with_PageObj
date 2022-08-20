import time


class BaseObj:
    def __init__(self, driver):
        self._driver = driver
        self._search_word = None

    locators_base = {"search_bar": "id=search_query_top",
                     "submit_search": 'xpath=//*[@id="searchbox"]/button',
                     "product_container": ".product-container"
                     }

    def search(self, search_word: str) -> ["webdriver"]:
        """
        go on top search bar and make a search of the search word
        :param search_word: str: the word need to search
        :return: [webdriver] : list of webdriver elements
        """
        self._driver.locator(self.locators_base["search_bar"]).fill(search_word)
        self._driver.locator(self.locators_base["submit_search"]).click()
        time.sleep(3)
        products_list = self._driver.query_selector_all(self.locators_base["product_container"])
        self._search_word = search_word
        return products_list

    @property
    def title(self) -> str:
        """
        get the title of this page
        :return: str : page title
        """
        return self._driver.title()

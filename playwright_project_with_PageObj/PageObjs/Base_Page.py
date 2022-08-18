import time



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
                "msg_confirm": ".cheque-indent",
                "forget_password":'text="Forgot your password?"'
                }

    def search(self, search_word: str) -> ["webdriver"]:
        """
        go on top search bar and make a search of the search word
        :param search_word: str: the word need to search
        :return: [webdriver] : list of webdriver elements
        """
        self._driver.locator(self.locators["search_bar"]).fill(search_word)
        self._driver.locator(self.locators["submit_search"]).click()
        time.sleep(3)
        products_list = self._driver.query_selector_all(self.locators["product_container"])
        return products_list
    @property
    def title(self) -> str:
        """
        get the title of this page
        :return: str : page title
        """
        return self._driver.title()

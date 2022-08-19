from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseObj:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 20)
        self._search_word = None

    locators = {"search_bar": (By.ID, "search_query_top"),
                "submit_search": (By.NAME, "submit_search"),
                "search_res": (By.ID, "center_column"),
                "product_container": (By.CLASS_NAME, "product-container"),
                "product_block": (By.CLASS_NAME, "right-block"),
                "product_details": (By.CLASS_NAME, "content_price"),
                "product_price": (By.TAG_NAME, "span"),
                "email": (By.ID, "email"),
                "password": (By.ID, "passwd"),
                "home": (By.CLASS_NAME, "home"),
                "SubmitLogin": (By.ID, "SubmitLogin"),
                "error_message_location": (By.CLASS_NAME, 'alert'),
                "error_text_message": (By.TAG_NAME, 'li'), "sign_In": (By.CLASS_NAME, "login"),
                "button_container": (By.CLASS_NAME, "button-container"),
                "add_to_cart": (By.TAG_NAME, "a"),
                "product_item": (By.TAG_NAME, "span"),
                "proceed_checkout": (By.LINK_TEXT, "Proceed to checkout"),
                "msg_confirm": (By.CLASS_NAME, "cheque-indent"),
                "proceed_checkout_buttons": (By.CLASS_NAME, "cart_navigation"),
                "proceed_checkout_order": (By.CLASS_NAME, "button"),
                "ship_check_box": (By.ID, "uniform-cgv"),
                "bank_wire_check": (By.CLASS_NAME, "bankwire"),
                "order_button_location": (By.ID, "cart_navigation"),
                "i_confirm_button": (By.TAG_NAME, "button"),
                "forgot_password": (By.LINK_TEXT, "Forgot your password?")
                }

    def search(self, search_word: str) -> [webdriver]:
        """
        go on top search bar and make a search of the search word
        :param search_word: str: the word need to search
        :return: [webdriver] : list of webdriver elements
        """
        self._driver.find_element(*self.locators["search_bar"]).send_keys(search_word)
        self.wait.until(EC.element_to_be_clickable(self.locators["submit_search"])).click()
        self.wait.until(EC.presence_of_element_located(self.locators["search_res"]))
        products_list = self._driver.find_elements(*self.locators["product_container"])
        self._search_word = search_word
        return products_list
    @property
    def title(self) -> str:
        """
        get the title of this page
        :return: str : page title
        """
        return self._driver.title

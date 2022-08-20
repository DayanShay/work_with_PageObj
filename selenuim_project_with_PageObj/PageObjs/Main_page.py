from selenium.webdriver.common.by import By
from selenuim_project_with_PageObj.PageObjs.Authentication_page import AuthenticationPage
from selenuim_project_with_PageObj.PageObjs.Base_Page import BaseObj
from selenuim_project_with_PageObj.PageObjs.Order_page import Orderpage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {"sign_In": (By.CLASS_NAME, "login"),
                "button_container": (By.CLASS_NAME, "button-container"),
                "add_to_cart": (By.TAG_NAME, "a"),
                "proceed_checkout": (By.LINK_TEXT, "Proceed to checkout"),
                "product_block": (By.CLASS_NAME, "right-block"),
                "product_details": (By.CLASS_NAME, "content_price"),
                "product_price": (By.TAG_NAME, "span"),
                }
    def sign_In(self) -> AuthenticationPage:
        """
        click on the singin  button
        :return: AuthenticationPage
        """
        self._driver.find_element(*self.locators["sign_In"]).click()
        return AuthenticationPage(self._driver)

    def find_cheap_from_search(self, product_containers) -> (str, "webdriver"):
        """
        find the cheapest item from the search results
        :param product_containers:
        :return: tuple(str,"webdriver"): the price and the item itself
        """
        if len(product_containers) == 0:
            raise Exception(f"No Products found in Search for -> {self._search_word}")
        price_list = {}
        for product_container in product_containers:
            right_block = product_container.find_element(*self.locators["product_block"])
            content_price = right_block.find_element(*self.locators["product_details"])
            price = content_price.find_element(*self.locators["product_price"]).text.strip()
            price_list[price.strip()] = right_block
        cheapest_price = min(price_list.keys())
        cheapest_dress = price_list[cheapest_price]
        return cheapest_price, cheapest_dress

    def click_add_to_cart(self, dress: "WebElement") -> None:
        """
        clicking on add to cart on the specific item
        :param dress: WebElement: the element in the page
        :return: None
        """
        dress.click()
        price_buttons = dress.find_element(*self.locators["button_container"])
        add_button = price_buttons.find_element(*self.locators["add_to_cart"])
        add_button.click()

    def click_proceed_to_checkout(self) -> Orderpage:
        """
        click on proceed to checkout on pop up window
        :return: Orderpage: the order page
        """
        self.wait.until(EC.presence_of_element_located(self.locators["proceed_checkout"])).click()
        return Orderpage(self._driver)

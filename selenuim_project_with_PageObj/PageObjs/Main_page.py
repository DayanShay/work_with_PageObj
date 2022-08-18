from selenium.webdriver.common.by import By
from selenuim_project_with_PageObj.PageObjs.Authentication_page import AuthenticationPage
from selenuim_project_with_PageObj.PageObjs.Base_Page import BaseObj
from selenuim_project_with_PageObj.PageObjs.Order_page import Orderpage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)

    def sign_In(self) -> AuthenticationPage:
        """
        click on the singin  button
        :return: AuthenticationPage
        """
        self._driver.find_element(*self.locators["sign_In"]).click()
        return AuthenticationPage(self._driver)

    def find_cheap_from_search(self, product_containers) -> (str,"webdriver"):
        """
        find the cheapest item from the search results
        :param product_containers:
        :return: tuple(str,"webdriver"): the price and the item itself
        """
        if len(product_containers) == 0:
            raise AssertionError("No Products found in Search Res")
        price_list = {}
        for product_container in product_containers:
            right_block = product_container.find_element(*self.locators["product_block"])
            content_price = right_block.find_element(*self.locators["product_details"])
            price = content_price.find_element(*self.locators["product_price"]).text.strip()
            price_list[price.strip()] = right_block
        cheapest_price = min(price_list.keys())
        cheapest_dress = price_list[cheapest_price]
        return cheapest_price, cheapest_dress

    def click_add_to_cart(self, dress:"WebElement")->None:
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

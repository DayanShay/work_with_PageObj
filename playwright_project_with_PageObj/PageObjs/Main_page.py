from playwright_project_with_PageObj.PageObjs.Authentication_page import AuthenticationPage
from playwright_project_with_PageObj.PageObjs.Base_Page import BaseObj
from playwright_project_with_PageObj.PageObjs.Order_page import Orderpage


class MainPage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)


    def SignIn(self) -> AuthenticationPage:
        """
        click on the singin  button
        :return: AuthenticationPage
        """
        self._driver.locator(self.locators["SignIn"]).click()
        return AuthenticationPage(self._driver)

    def find_cheap_from_search(self,product_containers) -> (str,str,"webdriver"):
        """
               find the cheapest item from the search results
               :param product_containers:
               :return: tuple(str,str,"webdriver"): the price and the name of the item and  the item itself
        """
        if len(product_containers) == 0:
            raise Exception("No Products found in Search Res")
        price_list = {}
        for product_container in product_containers:
            price = product_container.query_selector(self.locators["product_price"]).text_content().strip()
            price_list[price.strip()] = product_container
        cheapest_price = min(price_list.keys())
        cheapest_dress = price_list[cheapest_price]
        product_details = cheapest_dress.inner_text().split('\n')
        dress_name = product_details[0]
        return cheapest_price,dress_name,cheapest_dress

    def click_add_to_cart(self,dress)->None:
        """
        clicking on add to cart on the specific item
        :param dress: WebElement: the element in the page
        :return: None
        """
        dress.click()
        add_button = dress.query_selector(self.locators["add_to_cart"])
        add_button.click()

    def click_proceed_to_checkout(self)->Orderpage:
        """
        click on proceed to checkout on pop up window
        :return: Orderpage: the order page
        """
        proceed_checkout_button = self._driver.locator(self.locators["proceed_checkout"])
        proceed_checkout_button.click()
        return Orderpage(self._driver)


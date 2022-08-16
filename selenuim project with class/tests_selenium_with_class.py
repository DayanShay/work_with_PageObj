import pytest
from selenium import webdriver
from pages.Main_page import MainPage
from selenium.webdriver.common.by import By


path_driver = r"C:\Users\shaye\Desktop\study\selproject\chromedriver.exe"
url = r'http://automationpractice.com/index.php'


@pytest.fixture
def open_main_page():
    """
    This fixture - will open the page and will close it at the end. with yield.
    :return: None
    """
    driver = webdriver.Chrome(path_driver)
    driver.maximize_window()
    driver.get(url)
    yield MainPage(driver)
    driver.quit()


def test_buy_summer(open_main_page):
    Authentication_page = open_main_page.SignIn()
    MyAccount_page = Authentication_page.login("shay_dayan@gmail.com", "123456")
    main_page = MyAccount_page.home()
    products_list = main_page.search("summer")
    cheap_dress = main_page.find_cheap_from_search(products_list)
    main_page.click_add_to_cart(cheap_dress)
    order_page = main_page.click_proceed_to_checkout()
    order_page = order_page.complete_order()
    confirm_order_msg = order_page.get_confirm_msg()
    # confirm order need to be - > 'Your order on My Store is complete.' as the order_msg_templet
    assert confirm_order_msg == order_page._order_msg_templet
    print("YaBaLoLo")

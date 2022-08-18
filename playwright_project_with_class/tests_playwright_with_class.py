import pytest
import json
from playwright.sync_api import sync_playwright
from playwright_project_with_class.pages.Main_page import MainPage
import allure
import logging

MSG_info = logging.getLogger(__name__).info


@pytest.fixture
def get_data_for_test() -> json:
    try:
        with open('playwright_project_with_class/data_file_for_tests.json') as file_root:
            file_json_data = json.load(file_root)
    except:
        with open('data_file_for_tests.json') as file_root:
            file_json_data = json.load(file_root)
    finally:
        return file_json_data

@pytest.fixture
def open_main_page(get_data_for_test: json):
    """
    This fixture - will open the page and will close it at the end. with yield.
    :return: None
    """
    with sync_playwright() as p:
        if get_data_for_test["browser"] == "Chrome":
            browser = p.chromium.launch(headless=False)
        if get_data_for_test["browser"] == "Firefox":
            browser = p.firefox.launch(headless=False)
        if get_data_for_test["browser"] not in ("Firefox", "Chrome"):
            raise Exception(f"Browser Must be or 'Firefox' or 'Chrome' ONLY ! not -> {get_data_for_test['browser']}")
        driver = browser.new_page()
        driver.goto(get_data_for_test["url"])
        yield MainPage(driver)
        driver.close()



def test_buy_cheapest_dress_from_search(open_main_page: MainPage, get_data_for_test: json) -> None:
    """
    function log in the website and  find the cheapest product under a search word and complete Buying
    :param open_main_page: sync_playwright: website driver page
    :param get_data_for_test: json data content
    :return: None
    """
    MSG_info("Start Buy Cheap Dress")
    Authentication_page = open_main_page.SignIn()
    MyAccount_page = Authentication_page.login(get_data_for_test["email"], get_data_for_test["password"])

    MSG_info("You Have Logged in")

    main_page = MyAccount_page.home()
    products_list = main_page.search("summer")

    cheapest_price, dress_name, cheap_dress = main_page.find_cheap_from_search(products_list)
    MSG_info(f"Found the Cheap Dress : {dress_name} , And the Price is : {cheapest_price}")

    main_page.click_add_to_cart(cheap_dress)

    MSG_info(f"{dress_name} , Was added to Cart")

    MSG_info("Start the Buying Process")

    order_page = main_page.click_proceed_to_checkout()
    order_page = order_page.complete_order()
    confirm_order_msg = order_page.get_confirm_msg()

    MSG_info(f"{confirm_order_msg}")
    # confirm order need to be - > 'Your order on My Store is complete.' as the order_msg_templet
    assert confirm_order_msg == order_page._order_msg_templet


def test_log_in_with_wrong_password(open_main_page: MainPage, get_data_for_test: json) -> None:
    """
    test login with test_log_in_with_wrong_password details to website from get_data_for_test
    :param open_main_page:  sync_playwright: website driver page
    :param get_data_for_test: json data content
    :return: None
    """
    MSG_info(f"Start log_in_with_wrong_password")
    Authentication_page = open_main_page.SignIn()
    Authentication_page.login(get_data_for_test["email"], "a123asd12")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_wrong_password{error}")
    assert error[1] == "Authentication failed."


def test_log_in_with_invalid_email(open_main_page: MainPage) -> None:
    """
    test login with test_login_wrong details to website from get_data_for_test
    :param open_main_page:  sync_playwright: website driver page
    :return: None
    """
    MSG_info(f"Start log_in_with_invalid_email")
    Authentication_page = open_main_page.SignIn()
    Authentication_page.login("shay_dayanail.com", "123456")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_invalid_email{error}")
    assert error[1] == "Invalid email address."


def test_log_in_with_short_password(open_main_page: MainPage, get_data_for_test: json) -> None:
    """
    test login with test_login_wrong details to website
    :param open_main_page:  sync_playwright: website driver page
    :param get_data_for_test: json data content
    :return: None
    """
    MSG_info(f"Start log_in_with_short_password")
    Authentication_page = open_main_page.SignIn()
    Authentication_page.login(get_data_for_test["email"], "123")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_short_password{error}")
    assert error[1] == "Invalid password."


def test_log_in_with_no_details(open_main_page: MainPage) -> None:
    """
    test login with log_in_with_no_details details to website
    :param open_main_page:  MainPage: website driver page
    :return: None
    """
    MSG_info(f"Start log_in_with_no_details")
    Authentication_page = open_main_page.SignIn()
    Authentication_page.login("", "")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_no_details{error}")
    assert error[1] == "An email address required."


def test_log_in_with_right_details(open_main_page: MainPage, get_data_for_test: json) -> None:
    """
    test login with log_in_with_right_details details to website
    :param open_main_page:  MainPage: website driver page
    :param get_data_for_test: json data content

    :return: None
    """
    MSG_info(f"Start log_in_with_no_details")
    authentication_page = open_main_page.SignIn()
    my_account_page = authentication_page.login(get_data_for_test["email"], get_data_for_test["password"])
    MSG_info(f"Finish log_in_with_right_details {my_account_page._title}")
    assert my_account_page.title == my_account_page._title
def test_forget_password_button(open_main_page: MainPage) -> None:
    """
    function clicking on forget password in login form.
    :param open_main_page: sync_playwright: website driver page
    :return: None
    """
    MSG_info(f"Start test forget password button")

    Authentication_page = open_main_page.SignIn()
    Forget_Password_Page = Authentication_page.forget_password()
    assert Forget_Password_Page.title == Forget_Password_Page._title
    MSG_info(f"Finish test forget password button")
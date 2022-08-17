import pytest
import json
from playwright.sync_api import sync_playwright
from playwright_project_with_class.pages.Main_page import MainPage
import allure
import logging

MSG_info = logging.getLogger(__name__).info

path_driver = r"C:\Users\shaye\Desktop\study\selproject\chromedriver.exe"
url = r'http://automationpractice.com/index.php'

@pytest.fixture
def get_data_for_test():
    with open('data_file_for_tests.json') as file_root:
        file_json_data = json.load(file_root)
    return file_json_data

@pytest.fixture
def open_main_page(get_data_for_test,request):
    """
    This fixture - will open the page and will close it at the end. with yield.
    :return: None
    """
    if get_data_for_test["browser"] == "Chrome":
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            driver = browser.new_page()
            driver.goto("http://automationpractice.com/index.php")
            yield MainPage(driver)
            screen_shot_if_faild(driver, request)
            driver.close()
    if get_data_for_test["browser"] == "FireFox":
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            driver = browser.new_page()
            driver.goto("http://automationpractice.com/index.php")
            yield MainPage(driver)
            screen_shot_if_faild(driver, request)
            driver.close()

def screen_shot_if_faild(driver,request):
    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")

            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass  # just ignore

def test_buy_summer(open_main_page,get_data_for_test):
    MSG_info("Start Buy Cheap Dress")
    Authentication_page = open_main_page.SignIn()
    MyAccount_page = Authentication_page.login(get_data_for_test["email"],get_data_for_test["password"])

    MSG_info("You Have Logged in")

    main_page = MyAccount_page.home()
    products_list = main_page.search("summer")

    cheapest_price, cheap_dress = main_page.find_cheap_from_search(products_list)
    main_page.click_add_to_cart(cheap_dress)

    # editing the text in side the product text .

    product_details = cheap_dress.text.split('\n')
    MSG_info(f"Found the Cheap Dress : {product_details[0]} , And the Price is : {cheapest_price}")

    MSG_info("Start the Buying Process")

    order_page = main_page.click_proceed_to_checkout()
    order_page = order_page.complete_order()
    confirm_order_msg = order_page.get_confirm_msg()

    MSG_info(f"{confirm_order_msg}")
    # confirm order need to be - > 'Your order on My Store is complete.' as the order_msg_templet
    assert confirm_order_msg == order_page._order_msg_templet


def test_log_in_with_wrong_password(open_main_page,get_data_for_test):
    MSG_info(f"Start log_in_with_wrong_password")
    Authentication_page = open_main_page.SignIn()
    Authentication_page.login(get_data_for_test["email"], "a123asd12")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_wrong_password{error}")
    assert error[1] =="Authentication failed."


def test_log_in_with_invalid_email(open_main_page):
    MSG_info(f"Start log_in_with_invalid_email")
    Authentication_page = open_main_page.SignIn()
    Authentication_page.login("shay_dayanail.com", "123456")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_invalid_email{error}")
    assert error[1] =="Invalid email address."


def test_log_in_with_short_password(open_main_page):
    MSG_info(f"Start log_in_with_short_password")
    Authentication_page = open_main_page.SignIn()
    Authentication_page.login("shay_dayan@gmail.com", "123")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_short_password{error}")
    assert error[1] == "Invalid password."


def test_log_in_with_no_details(open_main_page):
    MSG_info(f"Start log_in_with_no_details")
    Authentication_page = open_main_page.SignIn()
    Authentication_page.login("", "")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_no_details{error}")
    assert error[1] =="An email address required."

def test_log_in_with_right_details(open_main_page,get_data_for_test):
    MSG_info(f"Start log_in_with_no_details")
    authentication_page = open_main_page.SignIn()
    my_account_page = authentication_page.login(get_data_for_test["email"],get_data_for_test["password"])
    MSG_info(f"Finish log_in_with_right_details {my_account_page._title}")
    assert my_account_page.get_title() == my_account_page._title


import pytest
import json
from selenium import webdriver
from selenuim_project_with_PageObj.PageObjs.Main_page import MainPage
import allure
import logging

MSG_info = logging.getLogger(__name__).info



@pytest.fixture
def get_data_for_test() -> json:
    """
    preparing data for the tests from json file.
    :return: json : data for tests.
    """
    try:
        with open('selenuim_project_with_PageObj/data_file_for_tests.json') as file_root:
            file_json_data = json.load(file_root)
    except:
        with open('data_file_for_tests.json') as file_root:
            file_json_data = json.load(file_root)
    finally:
        return file_json_data



@pytest.fixture
def open_main_page(get_data_for_test: json, request) -> None:
    """
    This fixture - will open the page and will close it at the end. with yield.
    :return: None
    """
    if get_data_for_test["browser"] == "Chrome":
        driver = webdriver.Chrome(get_data_for_test["path_driver"])
    if get_data_for_test["browser"] == "FireFox":
        driver = webdriver.Firefox(get_data_for_test["path_driver"])
        driver = webdriver.Firefox()
    if get_data_for_test["browser"] not in ("Firefox", "Chrome"):
        raise Exception(f"Browser Must be or 'Firefox' or 'Chrome' ONLY ! not -> {get_data_for_test['browser']}")

    driver.maximize_window()
    driver.get(get_data_for_test["url"])
    yield MainPage(driver)
    screenshot_if_faild(driver, request)
    driver.quit()


def screenshot_if_faild(driver: MainPage, request) -> None:
    """
    screenshot_if_faild takes a screenshot if a test faild
    :param driver:MainPage: the website we work on
    :param request: request: expect res of api
    :return:None
    """

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")

            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass  # just ignore


def test_buy_summer(open_main_page: MainPage, get_data_for_test: json) -> None:
    """
    function log in the website and  find the cheapest product under summer search and complete Buying
    :param open_main_page: sync_playwright: website driver page
    :param get_data_for_test: json data content
    :return: None
    """
    MSG_info("Start Buy Cheap Dress")
    authentication_page = open_main_page.sign_In()
    my_account_page = authentication_page.login(get_data_for_test["email"], get_data_for_test["password"])
    MSG_info("You Have Logged in")
    main_page = my_account_page.home()
    products_list = main_page.search(get_data_for_test["search_word"])
    cheapest_price, cheap_dress = main_page.find_cheap_from_search(products_list)
    product_details = cheap_dress.text.split('\n')
    MSG_info(f"Found the Cheap Dress : {product_details[0]} , And the Price is : {cheapest_price}")
    main_page.click_add_to_cart(cheap_dress)
    MSG_info(f"{product_details[0]} , Was added to Cart")
    MSG_info("Start the Buying Process")
    order_page = main_page.click_proceed_to_checkout()
    order_page = order_page.complete_order()
    confirm_order_msg = order_page.get_confirm_msg()
    MSG_info(f"{confirm_order_msg}")
    assert confirm_order_msg == order_page._order_msg_templet


def test_log_in_with_wrong_password(open_main_page: MainPage, get_data_for_test: json)-> None:
    """
    test login with test_log_in_with_wrong_password details to website from get_data_for_test
    :param open_main_page:  MainPage: website driver page
    :param get_data_for_test: json data content
    :return: None
    """
    MSG_info(f"Start log_in_with_wrong_password")
    Authentication_page = open_main_page.sign_In()
    Authentication_page.login(get_data_for_test["email"], "$4$3$3Ert")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_wrong_password{error}")
    assert error == "Authentication failed."


def test_log_in_with_invalid_email(open_main_page: MainPage)-> None:
    """
    test login with test_login_wrong details to website from get_data_for_test
    :param open_main_page:  MainPage: website driver page
    :return: None
    """
    MSG_info(f"Start log_in_with_invalid_email")
    Authentication_page = open_main_page.sign_In()
    Authentication_page.login("shay_dayanail.com", "123456")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_invalid_email{error}")

    assert error == "Invalid email address."


def test_log_in_with_short_password(open_main_page: MainPage, get_data_for_test: json):
    """
    test login with test_login_wrong details to website
    :param open_main_page:  sync_playwright: website driver page
    :param get_data_for_test: json data content
    :return: None
    """
    MSG_info(f"Start log_in_with_short_password")
    Authentication_page = open_main_page.sign_In()
    Authentication_page.login(get_data_for_test["email"], "123")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_short_password{error}")
    assert error == "Invalid password."


def test_log_in_with_no_details(open_main_page: MainPage) -> None:
    """
    test login with log_in_with_no_details details to website
    :param open_main_page:  MainPage: website driver page
    :return: None
    """
    MSG_info(f"Start log_in_with_no_details")
    Authentication_page = open_main_page.sign_In()
    Authentication_page.login("", "")
    error = Authentication_page.get_error_msg()
    MSG_info(f"Finish log_in_with_no_details{error}")
    assert error == "An email address required."


def test_log_in_with_right_details(open_main_page: MainPage, get_data_for_test: json) -> None:
    """
    test login with log_in_with_right_details details to website
    :param open_main_page:  MainPage: website driver page
    :param get_data_for_test: json data content

    :return: None
    """
    MSG_info(f"Start log_in_with_right_details")
    authentication_page = open_main_page.sign_In()
    my_account_page = authentication_page.login(get_data_for_test["email"], get_data_for_test["password"])
    MSG_info(f"Finish log_in_with_right_details")
    assert my_account_page.title == my_account_page._title


def test_forget_password_button(open_main_page: MainPage) -> None:
    """
    function clicking on forget password in login form.
    :param open_main_page: MainPage: website driver page
    :return: None
    """
    MSG_info(f"Start test forget password button")
    Authentication_page = open_main_page.sign_In()
    Forget_Password_Page = Authentication_page.forget_password()
    assert Forget_Password_Page.title == Forget_Password_Page._title
    MSG_info(f"Finish test forget password button")

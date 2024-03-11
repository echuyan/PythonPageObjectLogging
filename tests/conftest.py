import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import os
from pages.admin_login_page import AdminLoginPage
from pages.admin_logged_in_page import AdminLoggedInPage
from pages.catalogue_page import CataloguePage
from pages.main_page import MainPage
from pages.item_card_page import ItemCardPage
import random

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_opencart_url", default="http://localhost/oc/")

@pytest.fixture()
def open_random_featured_product(browser):
    featured_elements = MainPage(browser).get_featured_elements()
    random_index = random.randint(0, len(featured_elements) - 1)
    element = featured_elements[random_index]
    element.click()
    ItemCardPage(browser).get_title()

@pytest.fixture()
def open_catalogue(browser):
    CataloguePage(browser).get_narbar_menu()
    CataloguePage(browser).click_narbar_menu_element()
    CataloguePage(browser).click_see_all()
    yield

@pytest.fixture()
def open_catalogue_desktops(browser):
    MainPage(browser).get_featured_elements()
    MainPage(browser).click_desktops_row()
    MainPage(browser).show_desktops()
    yield


@pytest.fixture()
def receive_data():
    file_path = "../admin_credentials"
    file_descriptor = os.open(file_path, os.O_RDONLY)
    data = os.read(file_descriptor, os.path.getsize(file_path))
    print(data.decode())
    os.close(file_descriptor)
    return data.decode().split()

@pytest.fixture()
def login(receive_data, browser):
    data = receive_data
    AdminLoginPage(browser).input_username(data[0])
    AdminLoginPage(browser).input_password(data[1])
    AdminLoginPage(browser).click_button()
    try:
        AdminLoggedInPage(browser).get_modal()
        AdminLoggedInPage(browser).button_close_click()
        AdminLoggedInPage(browser).get_dashboard()
        AdminLoggedInPage(browser).get_nav_profile()
        return True
    except:
        return False

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_opencart_url = request.config.getoption("--base_opencart_url")

    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService()
        driver = webdriver.Chrome(service=service,options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "ya":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        binary_yandex_driver_file = '../drivers/yandexdriver.exe'
        driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
    driver.maximize_window()
    # driver.get(base_opencart_url)
    custom_url = request.node.get_closest_marker("url")
    if custom_url:
        driver.get(base_opencart_url+custom_url.args[0])
    else:
        driver.get(base_opencart_url)
    return driver




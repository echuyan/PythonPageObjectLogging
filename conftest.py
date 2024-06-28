import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import os
import pages.admin_login_page
from pages.admin_logged_in_page import AdminLoggedInPage
from pages.catalogue_page import CataloguePage
from pages.main_page import MainPage
from pages.item_card_page import ItemCardPage
import random
import logging
import datetime
import allure
import requests
import time

def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--headless", action="store_true")
    #parser.addoption("--base_opencart_url", default="https://demo.opencart.com/")
    parser.addoption("--base_opencart_url", default="https://192.168.65.254/oc")
    #parser.addoption("--base_opencart_url", default="https://127.0.0.1/oc")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--logs", action="store_true")
    #parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--executor", default="192.168.65.254")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")
    parser.addoption("--remote", action="store_true", default="TRUE")

@pytest.fixture()
@allure.title('Opening a random featured product on the main page (fixture)')
def open_random_featured_product(browser):
    featured_elements = MainPage(browser).get_featured_elements()
    random_index = random.randint(0, len(featured_elements) - 1)
    element = featured_elements[random_index]
    element.click()
    ItemCardPage(browser).get_title()

@pytest.fixture()
@allure.title('Opening catalogue from the main page (fixture)')
def open_catalogue(browser):
    CataloguePage(browser).get_narbar_menu()
    CataloguePage(browser).click_narbar_menu_element()
    CataloguePage(browser).click_see_all()
    yield

@pytest.fixture()
@allure.title('Opening Desktops section of the catalogue (fixture)')
def open_catalogue_desktops(browser):
    MainPage(browser).get_featured_elements()
    MainPage(browser).click_desktops_row()
    MainPage(browser).show_desktops()
    yield


@pytest.fixture()
@allure.title('Getting admin credentials from the file (fixture)')
def receive_data():
    file_path = "admin_credentials"
    file_descriptor = os.open(file_path, os.O_RDONLY)
    data = os.read(file_descriptor, os.path.getsize(file_path))
    print(data.decode())
    os.close(file_descriptor)
    return data.decode().split()

@pytest.fixture()
@allure.title('Logging in as an admin (fixture)')
def login(receive_data, browser):
    data = receive_data
    pages.admin_login_page.AdminLoginPage(browser).input_username(data[0])
    pages.admin_login_page.AdminLoginPage(browser).input_password(data[1])
    pages.admin_login_page.AdminLoginPage(browser).click_button()
    try:
        AdminLoggedInPage(browser).get_modal()
        AdminLoggedInPage(browser).button_close_click()
        AdminLoggedInPage(browser).get_dashboard()
        AdminLoggedInPage(browser).get_nav_profile()
        return True
    except:
        return False

@allure.step("Waiting for availability {url}")
def wait_url_data(url, timeout=10):
    """Метод ожидания доступности урла"""
    while timeout:
        response = requests.get(url)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if "video" in url:
                return response.content
            else:
                return response.text
    return None

@pytest.fixture()
@allure.title('Instantiating a browser (fixture)')
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_opencart_url = request.config.getoption("--base_opencart_url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    video = request.config.getoption("--video")
    #executor_url = f"http://{executor}:4444/wd/hub"
    executor_url = executor
    logs = request.config.getoption("--logs")
    remote = request.config.getoption("--remote")

    driver = None

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"tests/logs/{request.node.name}.log")
    #file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if remote == 'FALSE':
        #base_opencart_url = "http://localhost/oc/"
        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            service = ChromeService()
            driver = webdriver.Chrome(service=service,options=options)
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
        elif browser_name == "ya":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            binary_yandex_driver_file = 'drivers/yandexdriver.exe'
            driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
    else:
        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            service = ChromeService()
            #driver = webdriver.Chrome(service=service,options=options)
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("-headless")
            #driver = webdriver.Firefox(options=options)
        elif browser_name == "ya":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            binary_yandex_driver_file = 'drivers/yandexdriver.exe'
            #driver = webdriver.Chrome(binary_yandex_driver_file, options=options)

        capabilities = {
            "browserName": browser_name,
            #"browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc,
                "name": os.getenv("BUILD_NUMBER", str(random.randint(9000, 10000))),
                "screenResolution": "1280x2000",
                "enableVideo": video,
                "enableLog": logs,
                "timeZone": "Europe/Moscow",
                "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]

            },
            "acceptInsecureCerts": True,
        }
        for k, v in capabilities.items():
            options.set_capability(k, v)


            driver = webdriver.Remote(
                command_executor=executor_url,
                options=options
            )


    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    driver.maximize_window()

    custom_url = request.node.get_closest_marker("url")
    if custom_url:
        driver.get(base_opencart_url + custom_url.args[0])
    else:
        driver.get(base_opencart_url)

    return driver




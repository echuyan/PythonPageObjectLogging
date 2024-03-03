from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.item_card_page import ItemCardPage

# from page_objects.user_page import UserPage
# from page_objects.product_page import ProductPage
# from page_objects.cart_page import CartPage
# from page_objects.checkout_page import CheckoutPage
# from page_objects.comparison_page import ComparisonPage
# from page_objects.wish_list_page import WishListPage
# from page_objects.alert_element import AlertSuccessElement


# def test_add_to_cart(browser, db_connection):
#     product_name = MainPage(browser).get_featured_product_name(1)
#     MainPage(browser).click_featured_product(1)
#     ProductPage(browser).add_to_cart()
#     AlertSuccessElement(browser).shopping_cart.click()
#     CartPage(browser) \
#         .wait_for_product_in_cart(product_name) \
#         .click_checkout()
#     CheckoutPage(browser).click_login_page_link()
#     UserPage(browser).login(*create_random_user(db_connection))
#     CheckoutPage(browser).wait_page_load()


def test_check_title(browser):
    """
      Test is designed to check the title of the Main Page
    """
    MainPage(browser).wait_title_load("Your Store")


def test_check_featured(browser):
    """
        Test is designed to check the Featured Section of the Main Page
        Test id designed in a way to avoid StaleElementReferenceException
        Within the for loop the test opens each featured item card and checks its title
    """
    featured_elements = MainPage(browser).get_featured_elements()
    titles = MainPage(browser).get_img_titles()

    for i in range(len(featured_elements)):
        MainPage(browser).click_featured_product(i)
        ItemCardPage(browser).wait_page_load()
        ItemCardPage(browser).wait_title_load(titles[i])
        browser.back()
        i += 1


def test_check_nav_items(browser):
    """
        Test is designed to check the Navigation Bar of the Main Page

    """
    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-thumb")))
    nav_items_dropdown = browser.find_elements(By.XPATH, ("//li[@class='nav-item dropdown']"))
    nav_items = browser.find_elements(By.XPATH, ("//li[@class='nav-item']"))
    assert len(nav_items) != 0
    assert len(nav_items_dropdown) != 0


def test_check_carousel(browser):
    """
        Test is designed to check the carousel block of the Main Page

    """
    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "carousel-inner")))
    car_slides = browser.find_elements(By.XPATH, ("//div[@class='carousel slide']"))
    assert len(car_slides) == 2
    car_indicators = browser.find_elements(By.XPATH, ("//div[@class='carousel-indicators']"))
    assert len(car_indicators) == 2


def test_check_cart(browser):
    """
        Test is designed to check the presence of the cart at the Main Page

    """
    browser.get(browser.base_opencart_url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.presence_of_element_located((By.ID, "header-cart")))
    cart_text = browser.find_element(By.XPATH, ("//div[@id='header-cart']/div/button")).text
    assert cart_text == "0 item(s) - $0.00"



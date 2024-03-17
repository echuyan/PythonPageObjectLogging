from selenium.webdriver import ActionChains
from pages.main_page import MainPage
from pages.cart_page import CartPage
from selenium.webdriver.common.keys import Keys
import allure

@allure.epic('Working with cart')
@allure.title('Adding one item to cart')
def test_add_item_to_cart(browser):
    """
        Test is designed to check adding a random item from the main page to the cart
    """
    actions = ActionChains(browser)
    MainPage(browser).get_featured_elements()
    title = MainPage(browser).get_item_title_text()
    actions.send_keys(Keys.PAGE_DOWN)
    element1 = MainPage(browser).get_button_group()
    actions.move_to_element(element1).perform()
    addtocart = MainPage(browser).get_add_to_cart()
    actions.move_to_element(addtocart).click().perform()
    MainPage(browser).get_alert()
    MainPage(browser).click_header_cart_button()
    MainPage(browser).get_view_cart()
    MainPage(browser).get_checkout()

    items = CartPage(browser).get_cart_elements()
    titles = []
    for item in items:
        titles.append(item.text)

    assert title in titles


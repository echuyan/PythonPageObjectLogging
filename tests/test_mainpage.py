from pages.main_page import MainPage
from pages.item_card_page import ItemCardPage


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
    MainPage(browser).get_featured_elements()
    nav_items_dropdown = MainPage(browser).get_nav_items_dropdown()
    nav_items = MainPage(browser).get_nav_items()
    assert len(nav_items) != 0 and len(nav_items_dropdown) != 0


def test_check_carousel(browser):
    """
        Test is designed to check the carousel block of the Main Page

    """
    MainPage(browser).get_carousel()
    car_slides = MainPage(browser).get_carousel_slides()
    car_indicators = MainPage(browser).get_carousel_indicators()
    assert len(car_slides) == 2 and len(car_indicators) == 2


def test_check_cart(browser):
    """
        Test is designed to check the presence of the cart at the Main Page

    """
    MainPage(browser).get_header_cart()
    assert MainPage(browser).get_header_cart_text() == "0 item(s) - $0.00"



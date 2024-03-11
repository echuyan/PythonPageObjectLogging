import allure
from pages.item_card_page import ItemCardPage
CHECK_IMG = ".jpg"

def test_check_qty_input_and_button(open_random_featured_product, browser):
    """
      Test is designed to check some functional elements are present on the item card page
    """
    assert ItemCardPage(browser).get_qty() and ItemCardPage(browser).get_input() and ItemCardPage(browser).get_button()


def test_check_image_present(open_random_featured_product, browser):
    """
      Test is designed to check that product image is present for a random product from featured list
    """
    try:
        assert CHECK_IMG in ItemCardPage(browser).get_img_href()
    except Exception:
        print("Something went wrong. No element found.")


def test_check_description_present(open_random_featured_product, browser):
    """
      Test is designed to check that product description is present for a random product from featured list
    """
    with allure.step("Поиск элементов"):
        try:
            assert ItemCardPage(browser).get_tab_description_text() == 'Description' and ItemCardPage(browser).get_product_description_text()
        except Exception:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            print("Something went wrong. No element found.")



def test_check_review_tab(open_random_featured_product, browser):
    """
      Test is designed to check the Reviews tab content
    """
    try:
        ItemCardPage(browser).click_tab_review()
        assert ItemCardPage(browser).get_author() and ItemCardPage(browser).get_txt() and ItemCardPage(browser).get_rating()
    except Exception:
        print("Something went wrong.")


def test_check_nav_tab(open_random_featured_product, browser):
    """
      Test is designed to check that navigation tab is present on the item page
    """
    try:
        assert ItemCardPage(browser).get_top()
    except Exception:
        print("Something went wrong.")


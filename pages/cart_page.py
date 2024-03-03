from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CartPage(BasePage):
    SHOPPING_CART = By.XPATH, "//*[@id='shopping-cart']"
    CHECKOUT_LINK = By.LINK_TEXT, "Checkout"

    def _product_name(self, product_name):
        return By.XPATH, self.SHOPPING_CART[1] + self._text_xpath(product_name)

    def click_checkout(self):
        self.click(self.CHECKOUT_LINK)

    def wait_for_product_in_cart(self, product_name):
        self.get_element(self._product_name(product_name))
        return self
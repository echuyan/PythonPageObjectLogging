from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    __CART_ELEMENTS = By.XPATH, "//div[@id='shopping-cart']/div/table/tbody/tr/td[@class='text-start text-wrap']/a"

    def get_cart_elements(self):
        return self.get_elements(self.__CART_ELEMENTS)
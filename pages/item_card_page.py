from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ItemCardPage(BasePage):
    __TITLE = By.TAG_NAME,"title"
    __QUANTITY = By.XPATH, "//div[contains(text(), 'Qty')]"
    __INPUT = By.NAME, "quantity"
    __BUTTON =  By.ID, "button-cart"
    __IMG_TAG = By.XPATH, "//div[@class='image magnific-popup']/a"
    __PRODUCT_DESCRIPTION_TAG = By.XPATH, "//div[@id='tab-description']/p"
    __TAB_DESCRIPTION = By.XPATH, "//a[@href='#tab-description']"
    __TAB_REVIEW = By.XPATH, "//a[@href='#tab-review']"
    __AUTHOR = By.ID, "input-author"
    __TXT = By.ID, "input-text"
    __RATING = By.ID, "input-rating"
    __TOP = By.ID, "top"

    def get_title(self):
        return self.get_elements(self.__TITLE)

    def get_qty(self):
        return self.get_element(self.__QUANTITY)

    def get_input(self):
        return self.get_element(self.__INPUT)

    def get_button(self):
        return self.get_element(self.__BUTTON)

    def get_img_href(self):
        return self.get_element(self.__IMG_TAG).get_attribute("href")

    def get_tab_description_text(self):
        return self.get_element(self.__TAB_DESCRIPTION).text
    def get_product_description_text(self):
        return self.get_element(self.__PRODUCT_DESCRIPTION_TAG).text

    def click_tab_review(self):
        self.click(self.__TAB_REVIEW)

    def get_author(self):
        return self.get_element(self.__AUTHOR)

    def get_txt(self):
        return self.get_element(self.__TXT)

    def get_rating(self):
        return self.get_element(self.__RATING)


    def get_top(self):
        return self.get_element(self.__TOP)

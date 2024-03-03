from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ItemCardPage(BasePage):

    PRODUCT_INFO = By.ID, "product-info"
    TITLE = By.XPATH, "//head/title"
    PRODUCT_TITLE = By.XPATH, "//div[@id='content']/div/div/h1"
    def wait_page_load(self):

        self.get_element(self.PRODUCT_INFO)
    def get_featured_elements(self):
        return self.get_elements(self.FEATURED_ELEMENTS)

    def get_featured_product_name(self, index=0):
        return self.get_elements(self.FEATURED_PRODUCT_NAME)[index].text

    def get_img_elements_featured_products(self):
        return self.get_elements(self.IMG_ELEMENTS)

    def get_img_titles(self):
        return [item.get_attribute("title") for item in self.get_elements(self.IMG_ELEMENTS)]

    def click_featured_product(self, index=0):
        if index == 0:
            self.click(self.FEATURED_PRODUCT_NAME)
        else:
            self.get_elements(self.FEATURED_PRODUCT_NAME)[index].click()

    def _title_name(self, title_name):

        return By.XPATH, self.PRODUCT_TITLE[1] + self._text_xpath(title_name)#.replace("\"","")

    def wait_title_load(self, name):

        self.get_element(self._title_name(name))


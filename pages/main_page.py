from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    FEATURED_PRODUCT_NAME = By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a"
    TITLE = By.XPATH, "//head/title"
    FEATURED_ELEMENTS = By.CLASS_NAME, "product-thumb"
    IMG_ELEMENTS = By.XPATH, "//div[@class='product-thumb']/div/a/img"
    By.ID, "product-info"
    NAV_ITEMS_DROPDOWN = By.XPATH, ("//li[@class='nav-item dropdown']")
    NAV_ITEMS = By.XPATH, ("//li[@class='nav-item']")
    CAROUSEL = By.CLASS_NAME, "carousel-inner"
    CAROUSEL_SLIDES = By.XPATH, "//div[@class='carousel slide']"
    CAROUSEL_INDICATORS = By.XPATH, "//div[@class='carousel-indicators']"
    HEADER_CART = By.ID, "header-cart"
    HEADER_CART_BUTTON = By.XPATH, "//div[@id='header-cart']/div/button"
    __DESKTOPS = By.XPATH, "//div[@id='narbar-menu']/ul/li/a[contains(text(), 'Desktops')]"
    __SHOW_DESKTOPS = By.XPATH, "//div[@id='narbar-menu']/ul/li/a[contains(text(), 'Desktops')]/following-sibling::div/a"
    __ITEM_TITLE = By.XPATH, "//div/div/h4/a"
    __ADD_TO_CART_BUTTON = By.XPATH, "//div/form/div/button[@aria-label='Add to Cart']"
    __ALERT = By.XPATH, "//div[@id='alert']"
    __VIEW_CART = By.XPATH, "//strong[contains(text(), 'View Cart')]"
    __CHECKOUT = By.XPATH, "//strong[contains(text(), 'Checkout')]"
    __BUTTON_GROUP = By.XPATH, "//div[@class='button-group']"
    __PRICES = By.XPATH, "//span[@class='price-new']"
    __CURRENT_CUR = By.XPATH, "//form[@id='form-currency']/div/a/strong"
    __SWITCHER = By.XPATH, "//span[contains(text(),'Currency')]"
    __SWITCHES = By.XPATH, "//form[@id='form-currency']/div/ul/li/a"

    def get_switches(self):
        return self.get_elements(self.__SWITCHES)
    def click_switcher(self):
        self.get_element(self.__SWITCHER).click()
    def get_current_cur(self):
        return self.get_element(self.__CURRENT_CUR).text
    def get_prices(self):
        return self.get_elements(self.__PRICES)
    def get_button_group(self):
        return self.get_element(self.__BUTTON_GROUP)
    def get_view_cart(self):
        return self.get_element(self.__VIEW_CART)

    def get_checkout(self):
        return self.get_element(self.__CHECKOUT)
    def get_alert(self):
        return self.get_element(self.__ALERT)

    def get_add_to_cart(self):
      return self.get_element(self.__ADD_TO_CART_BUTTON)

    def get_item_title_text(self):
        return self.get_element(self.__ITEM_TITLE).text
    def show_desktops(self):
        self.click(self.__SHOW_DESKTOPS)
    def click_desktops_row(self):
        self.click(self.__DESKTOPS)
    def get_header_cart_text(self):
        return self.get_element(self.HEADER_CART_BUTTON).text
    def get_header_cart(self):
        return self.get_elements(self.HEADER_CART)
    def click_header_cart_button(self):
        self.get_element(self.HEADER_CART_BUTTON).click()
    def get_carousel_indicators(self):
        return self.get_elements(self.CAROUSEL_INDICATORS)
    def get_carousel_slides(self):
        return self.get_elements(self.CAROUSEL_SLIDES)
    def get_carousel(self):
        return self.get_elements(self.CAROUSEL)
    def get_nav_items(self):
        return self.get_elements(self.NAV_ITEMS)
    def get_nav_items_dropdown(self):
        return self.get_elements(self.NAV_ITEMS_DROPDOWN)

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
        self.logger.debug("Getting title name")
        return By.XPATH, self.TITLE[1] + self._text_xpath(title_name)

    def wait_title_load(self, name):

        self.get_element(self._title_name(name))


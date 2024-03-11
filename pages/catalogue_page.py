from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CataloguePage(BasePage):
    __NARBAR_MENU = By.ID, "narbar-menu"
    __NARBAR_MENU_ELEMENT = By.XPATH, "//div[@id='narbar-menu']/ul/li/a"
    __SEE_ALL = By.CLASS_NAME, "see-all"
    __ACTIVE_ELEMENT = By.XPATH,"//div/a[@class='list-group-item active']"
    __HEADING = By.XPATH, "//div[@id='content']/h1"
    __PAGINATION = By.CLASS_NAME, "pagination"
    __PAGINATION_TEXT = By.XPATH, "//div[@class='col-sm-6 text-end']"
    __PRODUCT_THUMBS = By.XPATH, "//div[@class='product-thumb']"
    __NEXT_PAGE = By.XPATH, "//a[contains(text(), '>') and not(contains(text(),'|'))]"
    __CATALOGUE_ITEMS_NON_COMPONENTS = By.XPATH, "//a[@class='list-group-item' and not(contains(text(), 'Components'))]"
    __CONTENT = By.XPATH, "//div[@id='content']"
    __ITEMS_BUTTONS = By.XPATH, "//button[@type='submit']"
    __CATALOGUE_ITEMS_NON_INNER = By.XPATH, "//a[@class='list-group-item' and not(contains(text(), '-')) and not(contains(text(), '0')) and not(contains(text(), 'Components'))]"
    __CATALOGUE_ITEMS = By.XPATH, "//a[@class='list-group-item']"
    __OPTIONS = By.XPATH, "//select[@id='input-limit']/option"
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

    def get_options(self):
        return self.get_elements(self.__OPTIONS)
    def get_catalogue_items(self):
        return self.get_elements(self.__CATALOGUE_ITEMS)
    def get_catalogue_items_non_inner(self):
        return self.get_elements(self.__CATALOGUE_ITEMS_NON_INNER)
    def get_items_buttons(self):
        return self.get_elements(self.__ITEMS_BUTTONS)
    def get_content(self):
        return self.get_elements(self.__CONTENT)
    def get_catalogue_items_non_components(self):
        return self.get_elements(self.__CATALOGUE_ITEMS_NON_COMPONENTS)
    def click_next_page(self):
        self.click(self.__NEXT_PAGE)
    def get_product_thumbs(self):
        return self.get_elements(self.__PRODUCT_THUMBS)
    def get_pagination_text(self):
        return self.get_element(self.__PAGINATION_TEXT).text

    def get_pagination(self):
        return self.get_element(self.__PAGINATION)
    def get_narbar_menu(self):
        return self.get_element(self.__NARBAR_MENU)

    def click_narbar_menu_element(self):
        self.click(self.__NARBAR_MENU_ELEMENT)

    def get_active_element_text(self):
        return self.get_element(self.__ACTIVE_ELEMENT).text

    def get_heading_text(self):
        return self.get_element(self.__HEADING).text
    def click_see_all(self):
        self.click(self.__SEE_ALL)

    def get_img_titles(self):
       return [item.get_attribute("title") for item in self.get_elements(self.IMG_ELEMENTS)]



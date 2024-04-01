from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
import random
import allure


class AdminLoggedInPage(BasePage):


    __MODAL = By.XPATH, "//body[@class='modal-open']"
    __BTN_CLOSE = By.XPATH, "//body[@class='modal-open']/descendant::button[@class='btn-close']"
    __DASHBOARD = By.XPATH, "//h1[text()='Dashboard']"
    __NAV_PROFILE = By.ID, "nav-profile"
    __LOGOUT = By.XPATH, "//span[text()='Logout']"
    __CATALOGUE = By.XPATH, "//a[text()=' Catalog']"
    __CATALOGUE_PROD_SUBMENU = By.XPATH, "//li[@id='menu-catalog']/ul/li/a[text()='Products']"
    __ADD_NEW_BUTTON = By.CSS_SELECTOR, '.float-end .btn.btn-primary'
    __PRODUCT_NAME = By.XPATH, "//input[@id='input-name-1']"
    __META_TAG = By.XPATH, "//input[@id='input-meta-title-1']"
    __DATA_TAB = By.XPATH, "//a[text()='Data']"
    __MODEL = By.XPATH, "//input[@id='input-model']"
    __PRICE = By.XPATH, "//input[@id='input-price']"
    __SEO_TAB = By.XPATH, "//a[text()='SEO']"
    __KEYWORD = By.XPATH, "//input[@id='input-keyword-0-1']"
    __SAVE_BUTTON = By.CSS_SELECTOR, '.float-end .btn.btn-primary'
    __SUCCESS = By.XPATH, "//div[@class='alert alert-success alert-dismissible']"
    __CHECKBOXES = By.XPATH, "//input[@type='checkbox']"
    __DELETE_BUTTON = By.CSS_SELECTOR, '.float-end .btn.btn-danger'

    @allure.step("Filling product data with given parameters to create a new product: name: '{product_name}', meta_tag: '{meta_tag}', model: '{model}', price: '{price}', keyword: '{keyword}' ")
    def fill_new_product_data(self, product_name: str, meta_tag: str, model: str, price: float,keyword: str):
        self.logger.debug("Filling product data with given parameters to create a new product: name: %s, meta_tag: %s, model: %s, price: %d, keyword: %s" %(product_name, meta_tag, model, price, keyword))
        self.get_element(self.__PRODUCT_NAME).send_keys(product_name)
        self.get_element(self.__META_TAG).send_keys(meta_tag)
        self.get_element(self.__DATA_TAB).click()
        self.get_element(self.__MODEL).send_keys(model)
        self.get_element(self.__PRICE).send_keys(price)
        self.get_element(self.__SEO_TAB).click()
        self.get_element(self.__KEYWORD, 1).send_keys(keyword)
        self.get_element(self.__SAVE_BUTTON).click()
        self.get_element(self.__SUCCESS)

    def delete_click(self):
        self.get_element(self.__DELETE_BUTTON).click()
    def click_random_checkbox(self):
        checkboxes = self.get_elements(self.__CHECKBOXES)
        checkboxes[random.randint(1, len(checkboxes) - 1)].click()

        time.sleep(4)

    def get_checkboxes(self):
        return self.get_elements(self.__CHECKBOXES)

    def get_add_new(self):
        return self.get_element(self.__ADD_NEW_BUTTON)
    def add_new_click(self):
        self.get_element(self.__ADD_NEW_BUTTON).click()
    def catalogue_prod_submenu_click(self):
        self.get_element(self.__CATALOGUE_PROD_SUBMENU).click()
    def catalogue_click(self):
        self.get_element(self.__CATALOGUE).click()

    def get_modal(self):
        return self.get_element(self.__MODAL)

    def get_dashboard(self):
        return self.get_element(self.__DASHBOARD)

    def get_nav_profile(self):
        return self.get_element(self.__NAV_PROFILE)

    def button_close_click(self):
        self.get_element(self.__BTN_CLOSE).click()

    def logout_click(self):
        self.get_element(self.__LOGOUT).click()
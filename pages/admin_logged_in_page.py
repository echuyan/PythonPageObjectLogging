from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminLoggedInPage(BasePage):


    __MODAL = By.XPATH, "//body[@class='modal-open']"
    __BTN_CLOSE = By.XPATH, "//body[@class='modal-open']/descendant::button[@class='btn-close']"
    __DASHBOARD = By.XPATH, "//h1[text()='Dashboard']"
    __NAV_PROFILE = By.ID, "nav-profile"
    __LOGOUT = By.XPATH, "//span[text()='Logout']"


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
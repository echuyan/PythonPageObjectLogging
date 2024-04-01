from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminLoginPage(BasePage):
    __INPUT_USERNAME = By.ID, "input-username"
    __PASSWORD = By.NAME, "password"
    __BUTTON = By.CSS_SELECTOR, "button[type='submit']"
    __OPEN_CART = By.XPATH, "//*[text()='OpenCart']"
    __CARD_HEADER = By.XPATH,"//div[@class='card-header']"


    def input_username(self,username: str):
        self.logger.debug("Sending usernaname")
        self.get_element(self.__INPUT_USERNAME).send_keys(username)

    def input_password(self, password: str):
        self.logger.debug("Sending password")
        self.get_element(self.__PASSWORD).send_keys(password)

    def click_button(self):
        self.get_element(self.__BUTTON).click()


    def get_input_username(self):
        return self.get_element(self.__INPUT_USERNAME)

    def get_password(self):
        return self.get_element(self.__PASSWORD)

    def get_button(self):
        return self.get_element(self.__BUTTON)

    def get_open_cart(self):
        return self.get_element(self.__OPEN_CART)

    def get_card_header_text(self):
        return self.get_element(self.__CARD_HEADER).text
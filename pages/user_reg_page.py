from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserRegPage(BasePage):
    __INPUT_FIRSTNAME = By.ID, "input-firstname"
    __INPUT_LASTNAME = By.ID, "input-lastname"
    __INPUT_EMAIL = By.ID, "input-email"
    __INPUT_PASSWORD = By.NAME, "password"
    __BUTTON_SUBMIT = By.CSS_SELECTOR, "button[type='submit']"
    __OPEN_CART = By.XPATH, "//*[text()='OpenCart']"
    __CONTENT_TEXT = By.XPATH, "//div[@id='content']/h1"

    def get_input_firstname(self):
        return self.get_element(self.__INPUT_FIRSTNAME)

    def get_input_lastname(self):
        return self.get_element(self.__INPUT_LASTNAME)

    def get_input_email(self):
        return self.get_element(self.__INPUT_EMAIL)
    def get_input_password(self):
        return self.get_element(self.__INPUT_PASSWORD)
    def get_button_submit(self):
        return self.get_element(self.__BUTTON_SUBMIT)
    def get_open_cart(self):
        return self.get_element(self.__OPEN_CART)

    def get_content_text(self):
        return self.get_element(self.__CONTENT_TEXT).text

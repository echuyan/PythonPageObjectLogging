from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import os
import json
import time

def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)

class UserRegPage(BasePage):
    __INPUT_FIRSTNAME = By.ID, "input-firstname"
    __INPUT_LASTNAME = By.ID, "input-lastname"
    __INPUT_EMAIL = By.ID, "input-email"
    __INPUT_PASSWORD = By.NAME, "password"
    __BUTTON_SUBMIT = By.CSS_SELECTOR, "button[type='submit']"
    __OPEN_CART = By.XPATH, "//*[text()='OpenCart']"
    __CONTENT_TEXT = By.XPATH, "//div[@id='content']/h1"
    __AGREE = By.XPATH, "//input[@type='checkbox' and @name='agree']"
    __SUCCESS = By.XPATH, "//h1[text()='Your Account Has Been Created!']"

    def fill_new_user_data(self, first_name: str, last_name: str, email: str, password: str):
        self.get_element(self.__INPUT_FIRSTNAME).send_keys(first_name)
        self.get_element(self.__INPUT_LASTNAME).send_keys(last_name)
        self.get_element(self.__INPUT_EMAIL).send_keys(email)
        self.get_element(self.__INPUT_PASSWORD).send_keys(password)
        self.get_element(self.__AGREE).click()
        self.get_element(self.__BUTTON_SUBMIT).click()

        with open(get_path('registered_users.json'), "a") as f:
            s = json.dumps([first_name,last_name,email,password], indent=4)
            f.write(s)

    def get_success(self):
        return self.get_element(self.__SUCCESS)

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

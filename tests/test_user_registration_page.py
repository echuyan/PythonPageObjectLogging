import pytest
from pages.user_reg_page import UserRegPage
import allure

@allure.epic('Checking locators')
@allure.title('Checking different locators on the user registration page')
@pytest.mark.url("/index.php?route=account/register")
def test_user_reg_page(browser):
    """
         Test is designed to check the User Registration page
    """
    UserRegPage(browser).get_input_firstname()
    UserRegPage(browser).get_input_lastname()
    UserRegPage(browser).get_input_email()
    UserRegPage(browser).get_input_email()
    UserRegPage(browser).get_button_submit()
    UserRegPage(browser).get_open_cart()
    assert UserRegPage(browser).get_content_text() == 'Register Account'

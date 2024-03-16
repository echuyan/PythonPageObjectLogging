from pages.admin_login_page import AdminLoginPage
import pytest

@pytest.mark.url("/admin")
def test_admin_login_page(browser):
    """
         Test is designed to check the Admin Login page
    """
    AdminLoginPage(browser).get_button()
    AdminLoginPage(browser).get_password()
    AdminLoginPage(browser).get_input_username()
    AdminLoginPage(browser).get_open_cart()
    assert AdminLoginPage(browser).get_card_header_text() == 'Please enter your login details.'

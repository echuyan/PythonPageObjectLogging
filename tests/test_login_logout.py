import pytest
import os
from pages.admin_login_page import AdminLoginPage
from pages.admin_logged_in_page import AdminLoggedInPage


############################################Fixtures############################################
@pytest.fixture()
def receive_data():
    file_path = "../admin_credentials"
    file_descriptor = os.open(file_path, os.O_RDONLY)
    data = os.read(file_descriptor, os.path.getsize(file_path))
    print(data.decode())
    os.close(file_descriptor)
    return data.decode().split()
############################################End of Fixtures############################################


@pytest.mark.url("/admin")
def test_login_logout_admin_page(receive_data, browser):
    """
         Test is designed to check the login-logout on the Admin Page
    """
    data = receive_data

    AdminLoginPage(browser).input_username(data[0])
    AdminLoginPage(browser).input_password(data[1])
    AdminLoginPage(browser).click_button()
    try:
        AdminLoggedInPage(browser).get_modal()
        AdminLoggedInPage(browser).button_close_click()
        AdminLoggedInPage(browser).get_dashboard()
        assert AdminLoggedInPage(browser).get_nav_profile()
        AdminLoggedInPage(browser).logout_click()
    except Exception:
        AdminLoggedInPage(browser).get_dashboard()
        assert AdminLoggedInPage(browser).get_nav_profile()
        AdminLoggedInPage(browser).logout_click()

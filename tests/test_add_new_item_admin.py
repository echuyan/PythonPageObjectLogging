import pytest
import os
from pages.admin_login_page import AdminLoginPage
from pages.admin_logged_in_page import AdminLoggedInPage
import random
import string


############################################Fixtures############################################
@pytest.fixture()
def receive_data():
    file_path = "../admin_credentials"
    file_descriptor = os.open(file_path, os.O_RDONLY)
    data = os.read(file_descriptor, os.path.getsize(file_path))
    print(data.decode())
    os.close(file_descriptor)
    return data.decode().split()

@pytest.fixture()
def login(receive_data,browser):
    data = receive_data
    AdminLoginPage(browser).input_username(data[0])
    AdminLoginPage(browser).input_password(data[1])
    AdminLoginPage(browser).click_button()
    try:
        AdminLoggedInPage(browser).get_modal()
        AdminLoggedInPage(browser).button_close_click()
        AdminLoggedInPage(browser).get_dashboard()
        AdminLoggedInPage(browser).get_nav_profile()
        return True
    except:
        return False
############################################End of Fixtures############################################


@pytest.mark.url("/admin")
def test_add_new_item_admin(browser,login):
    """
         Test is designed to check the Admin Login page
    """
    AdminLoggedInPage(browser).catalogue_click()
    AdminLoggedInPage(browser).catalogue_prod_submenu_click()
    AdminLoggedInPage(browser).get_add_new()
    AdminLoggedInPage(browser).add_new_click()
    AdminLoggedInPage(browser).fill_new_product_data("New Product","META TAG","MODEL",5.6,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))

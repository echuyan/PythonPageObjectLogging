import pytest
from pages.admin_logged_in_page import AdminLoggedInPage


@pytest.mark.url("/admin")
def test_delete_item_admin(browser, login):
    """
         Test is designed to check the Admin Login page
    """
    AdminLoggedInPage(browser).catalogue_click()
    AdminLoggedInPage(browser).catalogue_prod_submenu_click()
    AdminLoggedInPage(browser).click_random_checkbox()
    AdminLoggedInPage(browser).delete_click()
    alert = browser.switch_to.alert
    alert.accept()

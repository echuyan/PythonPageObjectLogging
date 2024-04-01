import time

import pytest

from pages.admin_logged_in_page import AdminLoggedInPage
import random
import string
import allure


@allure.epic('Working with catalogue')
@allure.title('Adding a new product to the catalogue with admin credentials')
@pytest.mark.url("/admin")
def test_add_new_item_admin(browser, login):
    """
         Test is designed to check the Admin Login page
    """
    with allure.step("Adding a new product"):
        AdminLoggedInPage(browser).catalogue_click()
        time.sleep(1)
        AdminLoggedInPage(browser).catalogue_prod_submenu_click()
        AdminLoggedInPage(browser).get_add_new()
        AdminLoggedInPage(browser).add_new_click()
        AdminLoggedInPage(browser).fill_new_product_data("New Product","META TAG","MODEL",5.6,''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))

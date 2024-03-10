import pytest
from pages.user_reg_page import UserRegPage
import random
import string


@pytest.mark.url("/index.php?route=account/register")
def test_user_reg_page(browser):
    """
         Test is designed to check the User Registration page
    """
    UserRegPage(browser).get_content_text() == 'Register Account'

    random_email =  ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6)) + '@test.com'

    UserRegPage(browser).fill_new_user_data(
        (''.join(random.choice(string.ascii_uppercase) for _ in range(12))),
        (''.join(random.choice(string.ascii_uppercase) for _ in range(15))),
        random_email,
        (''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6, 20)))
    )

    UserRegPage(browser).get_success()
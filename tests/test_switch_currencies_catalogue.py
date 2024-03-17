from pages.catalogue_page import CataloguePage
import allure

@allure.epic('Currencies')
@allure.title('Checking currency switching on the catalogue page')
def test_switch_cur_catalogue(open_catalogue, browser):
    """
        Test is designed to check currency switching at the catalogue page
    """

    prices = CataloguePage(browser).get_prices()
    old_prices = []
    for item in prices:
        old_prices.append(item.text)
    current_cur = CataloguePage(browser).get_current_cur()
    CataloguePage(browser).click_switcher()
    switches = CataloguePage(browser).get_switches()
    for switch in switches:
        if current_cur in switch.text:
            pass
        else:
            switch.click()
            break

    prices = CataloguePage(browser).get_prices()
    new_prices = []
    for item in prices:
        new_prices.append(item.text)
    old_set = set(old_prices)
    new_set = set(new_prices)
    assert old_set.isdisjoint(new_set)


from pages.main_page import MainPage
def test_switch_cur_main_page(browser):
    """
        Test is designed to check currency switching on the main page
    """
    MainPage(browser).get_featured_elements()
    prices = MainPage(browser).get_prices()
    old_prices=[]
    for item in prices:
        old_prices.append(item.text)
    current_cur = MainPage(browser).get_current_cur()
    MainPage(browser).click_switcher()
    switches = MainPage(browser).get_switches()
    for switch in switches:
        if current_cur in switch.text:
            pass
        else:
            switch.click()
            break
    prices = MainPage(browser).get_prices()
    new_prices = []
    for item in prices:
        new_prices.append(item.text)
    old_set = set(old_prices)
    new_set = set(new_prices)
    assert old_set.isdisjoint(new_set)


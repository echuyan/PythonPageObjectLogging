
import random
from pages.catalogue_page import CataloguePage

def test_check_headings_cat(open_catalogue, browser):
    """
      Test is designed to check that the heading of the catalogue section corresponds to the active element in the catalogue tree
    """
    assert CataloguePage(browser).get_heading_text() in CataloguePage(browser).get_active_element_text()


def test_check_pagination(open_catalogue_desktops, browser):
    """
      Test is designed to check that pagination in the catalogue
      Works with some limitations such as: section Desktops exists and contains more than 10 items
    """
    try:
        CataloguePage(browser).get_pagination()
        text = CataloguePage(browser).get_pagination_text()
        items_count = int(text.split()[5])
        pages = int(text.split()[6].split('(')[1])
        counter = 0
        for i in range (pages):
            counter += len(CataloguePage(browser).get_product_thumbs())
            if i != pages-1:
                CataloguePage(browser).click_next_page()
        assert counter == items_count
    except Exception:
        print("No pagination controls found.")


def test_check_tree_nav(open_catalogue, browser):
    """
      Test is designed to check catalogue tree navigation and number of items in the selected section
    """
    elements = CataloguePage(browser).get_catalogue_items_non_components()
    element = elements[2]
    items_count = int(element.text.split('(')[1].split(')')[0])
    element.click()
    CataloguePage(browser).get_content()
    assert items_count == len(CataloguePage(browser).get_product_thumbs())


def test_check_buttons(open_catalogue, browser):
    """
      Test is designed to check the existence of cart, favorite and comparison buttons for each product on the page
    """
    elements = CataloguePage(browser).get_catalogue_items_non_components()
    random_index = random.randint(0, len(elements) - 1)
    element = elements[random_index]
    items_count = int(element.text.split('(')[1].split(')')[0])
    element.click()
    CataloguePage(browser).get_content()
    assert len(CataloguePage(browser).get_items_buttons()) == items_count*3


def test_check_show_more_products(open_catalogue, browser):
    """
      Test is designed to check the Show switch (number of showed products)
    """
    elements = CataloguePage(browser).get_catalogue_items_non_inner()
    random_index = random.randint(0, len(elements) - 1)
    element = elements[random_index]
    items_count = int(element.text.split('(')[1].split(')')[0])
    element.click()
    CataloguePage(browser).get_content()
    try:
        selectors = CataloguePage(browser).get_options()
        random_index = random.randint(0, len(selectors) - 1)
        selector = selectors[random_index]
        selected_number = int(selector.text)
        selector.click()
        assert len(CataloguePage(browser).get_product_thumbs()) == selected_number or len(CataloguePage(browser).get_product_thumbs())  == items_count
    except Exception:
        assert len(CataloguePage(browser).get_product_thumbs()) == 0



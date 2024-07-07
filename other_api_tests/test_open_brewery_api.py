import pytest
from other_api_tests.base_request import BaseRequest
import random
import allure

BASE_URL_BREWERIES = 'https://api.openbrewerydb.org/v1'

@allure.epic('Open brewery')
@allure.title('Get all breweries')
def test_get_all_breweries():
    base_request = BaseRequest(BASE_URL_BREWERIES)
    breweries_list = base_request.get('breweries', "", expected_error=False)
    assert breweries_list

@allure.epic('Open brewery')
@allure.title('Get breweries by city per page')
@pytest.mark.parametrize("perpage, expected", [(2, 2), (1, 1)])
def test_get_breweries_by_city_per_page(get_cities, perpage, expected):
    base_request = BaseRequest(BASE_URL_BREWERIES)
    city = random.choice(list(get_cities))
    result = base_request.get(f'breweries?by_city={city}&per_page={perpage}', "", expected_error=False)
    assert len(result)==expected


@allure.epic('Open brewery')
@allure.title('Get breweries by type')
@pytest.mark.parametrize("type, expected", [("micro", "micro"), ("proprietor", "proprietor"), ("nano", "nano"), ("brewpub", "brewpub"), ("regional", "regional")])
def test_get_breweries_by_type(type, expected):
    base_request = BaseRequest(BASE_URL_BREWERIES)
    endpoint = f'breweries?by_type={type}&per_page=3'
    result = base_request.get(endpoint, "", expected_error=False)
    types1 = list({item["brewery_type"] for item in result})
    #types2 = [item["brewery_type"] for item in result]
    assert len(types1) == 1 and types1[0] == expected



@allure.epic('Open brewery')
@allure.title('Get random brewery')
@pytest.mark.parametrize("number, expected", [(3, 3), (52, 50)])
def test_get_random_brewery(number, expected):
    base_request = BaseRequest(BASE_URL_BREWERIES)
    endpoint = 'breweries/random'
    result = base_request.get(endpoint, "", expected_error=False)
    assert len(result)==1


@allure.epic('Open brewery')
@allure.title('Get brewery from non-existent city')
def test_get_non_existent_city():
    base_request = BaseRequest(BASE_URL_BREWERIES)
    endpoint = 'breweries?by_city=NON_EXIST'
    result = base_request.get(endpoint, "", expected_error=False)
    assert len(result) == 0



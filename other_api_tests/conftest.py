import pytest
from other_api_tests.base_request import BaseRequest
from collections import Counter

BASE_URL_BREWERIES = 'https://api.openbrewerydb.org/v1'
@pytest.fixture(scope="session")
def get_cities():
    base_request = BaseRequest(BASE_URL_BREWERIES)
    breweries_list = base_request.get('breweries?per_page=200', "", expected_error=False)
    cities = [item["city"] for item in breweries_list]
    city_counts = Counter(cities)
    filtered_cities = {city for city, count in city_counts.items() if count > 2}
    return filtered_cities
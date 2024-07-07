import allure
import pytest
import requests

from google_classrom_api_tests.conftest import move_to_acrhived_and_delete, generate_random_string
from google_classrom_api_tests.const import *


url = COURSES_API_ENDPOINT

@allure.epic('Get courses API')
@allure.title('Checking  GET method on courses')
def test_get_course(get_access_token, fixture_create_course):
    """
      Test is designed to check if information on the course can be retrieved
    """
    token = get_access_token
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    course_id = fixture_create_course
    response = requests.get(url+f"/{course_id}", headers=headers)

    print(response.json())
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()["id"] == course_id


@allure.epic('Get courses API')
@allure.title('Checking  GET method on non-existent course')
def test_get_non_existent_course(get_access_token, fixture_create_course):
    """
      Test is designed to check if information on the non-existent course can be retrieved
    """
    token = get_access_token
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    course_id = "non-existent"
    response = requests.get(url+f"/{course_id}", headers=headers)

    print(response.json())
    assert response.status_code == 404
    assert response.json() is not None
    assert response.json()["error"]["message"] == "Requested entity was not found."
    assert response.json()["error"]["status"] == "NOT_FOUND"


@allure.epic('Get courses API')
@allure.title('Checking  GET method without authentication')
def test_get_course_no_auth(fixture_create_course):
    """
      Test is designed to check  GET method without authentication
    """
    token = "FAKE_TOKEN"
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    course_id = "non-existent"
    response = requests.get(url+f"/{course_id}", headers=headers)

    print(response.json())
    assert response.status_code == 401
    assert response.json() is not None
    assert response.text.find("Request had invalid authentication credentials. Expected OAuth 2 access token, login cookie or other valid authentication credential.")
    assert response.json()["error"]["status"] == "UNAUTHENTICATED"
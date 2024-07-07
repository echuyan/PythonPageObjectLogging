import pytest
import allure
from google_classrom_api_tests.const import *
import google.auth.transport.requests
from google.oauth2 import service_account
import requests
import random
import string

url = COURSES_API_ENDPOINT

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def move_to_acrhived_and_delete(courseid, access_token, name):
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }
    body = {
        "courseState": "ARCHIVED",
        "name": name
    }

    response = requests.put(url + f'/{courseid}',  headers=headers, json=body)
    if response.status_code == 200:
        response = requests.delete(url + f'/{courseid}', headers=headers)

@pytest.fixture(scope="module")
@allure.title('Obtaining a Google OAuth2 Authorization token')
def get_access_token():

    credentials = service_account.Credentials.from_service_account_file(
        JSON_KEY, scopes=SCOPES)
    credentials.refresh(google.auth.transport.requests.Request())

    access_token = credentials.token
    return access_token


@pytest.fixture(scope="module")
@allure.title('Create test course')
def fixture_create_course(get_access_token):
    token = get_access_token
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    name = generate_random_string(7)
    section = generate_random_string(7)
    description = generate_random_string(17)

    course_data = {
        "name": name,
        "section": section,
        "descriptionHeading": "Heading",
        "description": description,
        "ownerId": "me",
        "courseState": CourseStates.PROVISIONED.value
    }

    response = requests.post(url, headers=headers, json=course_data)

    yield response.json()["id"]
    move_to_acrhived_and_delete(response.json()["id"], token, name)


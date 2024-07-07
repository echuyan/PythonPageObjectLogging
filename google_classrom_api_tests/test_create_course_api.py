import allure
import pytest
import requests

from google_classrom_api_tests.conftest import move_to_acrhived_and_delete, generate_random_string
from google_classrom_api_tests.const import *
import random
import string

url = COURSES_API_ENDPOINT

@allure.epic('Create courses API')
@allure.title('Checking  creation of the course')
def test_create_course(get_access_token):
    """
      Test is designed to check creation of the course
    """
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

    print(response.json())
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()["name"] == name
    assert response.json()["section"] == section
    move_to_acrhived_and_delete(response.json()["id"], token, name)

@allure.epic('Create courses API')
@allure.title('Checking  creation of the course with illegal state')
@pytest.mark.parametrize("state",[CourseStates.ACTIVE.value, CourseStates.ARCHIVED.value, CourseStates.DECLINED.value])
def test_create_course_with_illegal_state(get_access_token, state):
    """
      Test is designed to check creation of the course with states that are not allowed
    """
    headers = {
        'Authorization': 'Bearer ' + get_access_token,
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
        "courseState": state
    }

    response = requests.post(url, headers=headers, json=course_data)

    print(response.json())
    assert response.status_code == 403
    assert response.text.find('@CourseStateDenied')

@allure.epic('Create courses API')
@allure.title('Checking  creation of the course with illegal field')
def test_create_course_with_illegal_automatic_fields(get_access_token):
    """
      Test is designed to check creation of the course provided with fields that have to be filled automatically
    """
    headers = {
        'Authorization': 'Bearer ' + get_access_token,
        'Content-Type': 'application/json'
    }
    name = generate_random_string(7)
    section = generate_random_string(7)
    description = generate_random_string(17)

    course_data = {
        "id": "2141",
        "name": name,
        "section": section,
        "descriptionHeading": "Heading",
        "description": description,
        "creationTime": "2014-10-02T15:01:23Z",
        "updateTime": "2014-10-02T15:01:23Z",
        "ownerId": "me",
        "courseState": CourseStates.PROVISIONED.value
    }

    response = requests.post(url, headers=headers, json=course_data)

    print(response.json())
    assert response.status_code == 400
    assert response.text.find('INVALID_ARGUMENT')


@allure.epic('Create courses API')
@allure.title('Checking  creation of the course without obligatory fields')
def test_create_course_without_obligatory_fields(get_access_token):
    """
      Test is designed to check creation of the course without obligatory fields
    """
    headers = {
        'Authorization': 'Bearer ' + get_access_token,
        'Content-Type': 'application/json'
    }
    name = generate_random_string(7)
    section = generate_random_string(7)
    description = generate_random_string(17)

    course_data = {
        "section": section,
        "descriptionHeading": "Heading",
        "description": description,
        "ownerId": "me",
        "courseState": CourseStates.PROVISIONED.value
    }

    response = requests.post(url, headers=headers, json=course_data)

    print(response.json())
    assert response.status_code == 400
    assert response.text.find('INVALID_ARGUMENT')
    assert response.text.find("Course name must be specified.")


@allure.epic('Create courses API')
@allure.title('Checking  creation of the course with unknown fields provided')
def test_create_course_with_unknown_fields(get_access_token):
    """
      Test is designed to check creation of the course with unknown fields provided
    """
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
        "courseState": CourseStates.PROVISIONED.value,
        "unknownField": "unknown"
    }

    response = requests.post(url, headers=headers, json=course_data)

    print(response.json())
    assert response.status_code == 400
    assert response.text.find("Invalid JSON payload received.")

import allure
import pytest
import requests

from google_classrom_api_tests.conftest import move_to_acrhived_and_delete, generate_random_string
from google_classrom_api_tests.const import *


url = COURSES_API_ENDPOINT

@allure.epic('Create courses API')
@allure.title('Checking  update of the course')
def test_update_course(get_access_token, fixture_create_course):
    """
      Test is designed to check update of the course - updating name, section, status
    """
    token = get_access_token
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    course_id = fixture_create_course

    new_name = generate_random_string(7)
    new_section = generate_random_string(7)
    new_description = generate_random_string(17)
    new_status = CourseStates.ACTIVE.value

    course_data = {
        "name": new_name,
        "section": new_section,
        "description": new_description,
        "courseState": str(new_status)
    }

    response = requests.put(url+f"/{course_id}", headers=headers, json=course_data)

    print(response.json())
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()["name"] == new_name
    assert response.json()["section"] == new_section
    assert response.json()["status"] == new_status
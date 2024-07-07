import pytest
from other_api_tests.base_request import BaseRequest
import random
import allure

BASE_URL_JSON = 'https://jsonplaceholder.typicode.com'

@allure.epic('JSON placeholder')
@allure.title('Get all posts')
def test_get_all_posts():
    base_request = BaseRequest(BASE_URL_JSON)
    result = base_request.get('posts', "", expected_error=False)
    assert result is not None


@allure.epic('JSON placeholder')
@allure.title('Post a post')
def test_post_post():
    base_request = BaseRequest(BASE_URL_JSON)
    body = {
    "title": "foo",
    "body": "bar",
    "userId": "1"
}
    result = base_request.post('posts',"",body,expected_error=True)
    assert result['id'] is not None



@allure.epic('JSON placeholder')
@allure.title('Get resources')
def get_resources():
    base_request = BaseRequest(BASE_URL_JSON)
    res_list = base_request.get('posts', "", expected_error=False)
    ids = [item["id"] for item in res_list]
    return ids



@allure.epic('JSON placeholder')
@allure.title('Update all resources')
@pytest.mark.parametrize("id", get_resources(), scope="module")
def test_update_all_resources(id):
     base_request = BaseRequest(BASE_URL_JSON)
     body = {
         "id":"101",
         "title": "foo",
         "body": "bar",
         "userId": "1"
     }

     result = base_request.put(f'posts/{id}', "", body, expected_error=False)
     assert result is not None

@allure.epic('JSON placeholder')
@allure.title('Get two random resources')
def get_two_random_resources():
    base_request = BaseRequest(BASE_URL_JSON)
    res_list = base_request.get('posts', "", expected_error=False)
    ids = [item["id"] for item in res_list]
    id1 = random.choice(ids)
    id2 = random.choice(ids)
    return [id1,id2]

@allure.epic('JSON placeholder')
@allure.title('Delete random resource')
@pytest.mark.parametrize("id", get_two_random_resources(), scope="module")
def test_delete_random_resource(id):
    base_request = BaseRequest(BASE_URL_JSON)
    result = base_request.delete(f'posts/{id}', "")
    assert result is not None


@allure.epic('JSON placeholder')
@allure.title('Get nested resources')
def test_get_nested_resources():
    base_request = BaseRequest(BASE_URL_JSON)
    endpoint = 'posts/1/comments'
    result = base_request.get(endpoint, "", expected_error=False)
    emails = [item["email"] for item in result]
    assert "Eliseo@gardner.biz" in emails
    #assert result is not None


import allure
from client.api_client import ApiClient
from client.endpoints import endpoints
from models.user import UserCreate, UserResponse


@allure.feature("Users")
@allure.story("Create User")
def test_create_user(api: ApiClient):
    body = UserCreate(name="morpheus", job="leader").model_dump()
    resp = api.post(endpoints.USERS, json=body, expected_status=201)

    parsed = UserResponse(**resp.json())
    assert parsed.name == "morpheus"
    assert parsed.job == "leader"

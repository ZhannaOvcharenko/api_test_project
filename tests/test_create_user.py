import allure
from client.endpoints import USERS
from models.user import CreateUserRequest, CreateUserResponse

@allure.story("POST /users — создание пользователя")
def test_create_user_success(api):
    body = CreateUserRequest(name="morpheus", job="leader").model_dump()
    resp = api.post(USERS, json=body, expected_status=201)

    assert resp.status_code == 201

    created = CreateUserResponse.model_validate(resp.json())

    assert created.name == "morpheus"
    assert created.job == "leader"
    assert created.id
    assert created.createdAt
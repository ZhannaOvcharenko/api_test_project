import allure
from client.endpoints import LOGIN
from models.user import LoginRequest, LoginResponse

@allure.story("POST /login — авторизация и получение токена")
def test_login_success(api):
    payload = LoginRequest(email="eve.holt@reqres.in", password="pistol").model_dump()
    resp = api.post(LOGIN, json=payload, expected_status=200)

    assert resp.status_code == 200

    token = LoginResponse.model_validate(resp.json()).token

    assert token and isinstance(token, str)
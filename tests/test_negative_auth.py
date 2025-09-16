import allure
from client.endpoints import LOGIN
from models.user import LoginRequest, ErrorResponse


@allure.story("POST /login — негативный сценарий (нет пароля)")
def test_login_without_password_returns_400(api):
    payload = {"email": "Kristen@styart"}  # отсутствие поля password
    resp = api.post(LOGIN, json=payload, expected_status=400)

    assert resp.status_code == 400

    err = ErrorResponse.model_validate(resp.json())
    assert err.error.lower() == "missing password"

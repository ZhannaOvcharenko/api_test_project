import pytest
import allure
from client.api_client import ApiClient
from client.endpoints import endpoints
from models.user import LoginRequest, LoginResponse


@allure.feature("Auth")
@allure.story("Login")
def test_successful_login(api: ApiClient):
    body = LoginRequest(email="eve.holt@reqres.in", password="cityslicka").model_dump()
    resp = api.post(endpoints.LOGIN, json=body, expected_status=200)
    parsed = LoginResponse(**resp.json())
    assert parsed.token is not None


@allure.feature("Auth")
@allure.story("Login")
@pytest.mark.parametrize("missing_field", ["email", "password"])
def test_login_missing_field(api: ApiClient, missing_field):
    body = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    body.pop(missing_field)
    resp = api.post(endpoints.LOGIN, json=body, expected_status=400)

    error_text = resp.json()["error"]
    if missing_field == "email":
        assert error_text == "Missing email or username"
    else:
        assert error_text == "Missing password"


@allure.feature("Auth")
@allure.story("Login negative cases")
@pytest.mark.parametrize(
    "body, expected_error",
    [
        ({"email": "peter@klaven"}, "Missing password"),
        ({"password": "cityslicka"}, "Missing email or username"),
        ({}, "Missing email or username"),
    ],
)
def test_login_negative(api: ApiClient, body, expected_error):
    resp = api.post(endpoints.LOGIN, json=body, expected_status=400)
    from models.user import ErrorResponse
    parsed = ErrorResponse(**resp.json())
    assert parsed.error == expected_error

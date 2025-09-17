import allure
import pytest
from client.api_client import ApiClient
from client.endpoints import endpoints
from models.user import ErrorResponse


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
    parsed = ErrorResponse(**resp.json())
    assert parsed.error == expected_error

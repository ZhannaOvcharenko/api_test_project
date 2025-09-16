import allure
from client.endpoints import USERS
from models.user import ListUsersResponse


@allure.story("GET /users — список пользователей")
def test_get_users_returns_valid_schema(api):
    params = {"page": 2}
    resp = api.get(USERS, params=params, expected_status=200)

    assert resp.status_code == 200

    parsed = ListUsersResponse.model_validate(resp.json())

    assert parsed.page == 2
    assert len(parsed.data) > 0
    assert parsed.support.url

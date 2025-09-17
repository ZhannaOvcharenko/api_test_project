import allure
from client.api_client import ApiClient
from client.endpoints import endpoints
from models.user import UserListResponse


@allure.feature("Users")
@allure.story("Get Users")
def test_get_users(api: ApiClient):
    resp = api.get(endpoints.USERS, params={"page": 2}, expected_status=200)

    parsed = UserListResponse(**resp.json())

    assert len(parsed.data) > 0
    assert all(u.id is not None for u in parsed.data)

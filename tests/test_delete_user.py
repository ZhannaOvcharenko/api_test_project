import allure
from client.api_client import ApiClient
from client.endpoints import endpoints


@allure.feature("Users")
@allure.story("Delete User")
def test_delete_user(api: ApiClient):
    resp = api.delete(endpoints.USER_BY_ID.format(id=2), expected_status=204)
    assert resp.text == ""

import allure
from client.endpoints import USER_BY_ID

@allure.story("DELETE /users/{id} — удаление пользователя")
def test_delete_user_returns_204(api):
    resp = api.delete(USER_BY_ID.format(id=2), expected_status=204)
    assert resp.status_code == 204
    assert resp.text == ""
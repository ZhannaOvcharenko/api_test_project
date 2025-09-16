import os
import logging
import requests
import pytest
from dotenv import load_dotenv
from selene import browser

from client.api_client import ApiClient
from utils.config import setup_logging
from models.user import LoginRequest
from client.endpoints import LOGIN

load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def configure_base_url():
    api_base = os.getenv("API_BASE_URL", "https://reqres.in/api")
    browser.config.base_url = api_base
    setup_logging()
    yield


@pytest.fixture(scope="session")
def api() -> ApiClient:
    timeout = int(os.getenv("API_TIMEOUT", "15"))

    session = requests.Session()
    api_key = os.getenv("API_KEY", "reqres-free-v1")
    session.headers.update({"x-api-key": api_key})

    return ApiClient(session=session, timeout=timeout, logger=logging.getLogger("api"))


@pytest.fixture(scope="session")
def auth_token(api: ApiClient) -> str:
    email = os.getenv("AUTH_EMAIL", "eve.holt@reqres.in")
    password = os.getenv("AUTH_PASSWORD", "pistol")
    payload = LoginRequest(email=email, password=password).model_dump()

    resp = api.post(LOGIN, json=payload, expected_status=200)
    token = resp.json().get("token", "")

    os.makedirs("reports", exist_ok=True)
    with open("reports/api_token.txt", "w", encoding="utf-8") as f:
        f.write(token)

    return token

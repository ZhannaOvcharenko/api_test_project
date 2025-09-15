from __future__ import annotations
import time
import requests
import logging
from urllib.parse import urljoin
from typing import Any, Optional

from selene import browser
from utils.allure_helpers import attach_request, attach_response

class ApiClient:
    def __init__(self, session: Optional[requests.Session] = None, timeout: int = 15, logger: Optional[logging.Logger] = None):
        self.session = session or requests.Session()
        self.timeout = timeout
        self.logger = logger or logging.getLogger(__name__)

    @property
    def base_url(self) -> str:
        return browser.config.base_url

    def _full_url(self, endpoint: str) -> str:
        return urljoin(self.base_url.rstrip('/')+'/', endpoint.lstrip('/'))

    def request(self, method: str, endpoint: str, *, params: dict | None = None, json: Any = None,
                headers: dict | None = None, expected_status: int | None = None) -> requests.Response:
        url = self._full_url(endpoint)

        attach_request(method, url, headers, params, json)

        start = time.perf_counter()
        resp = self.session.request(method=method, url=url, params=params, json=json, headers=headers, timeout=self.timeout)
        elapsed_ms = int((time.perf_counter() - start) * 1000)

        try:
            body = resp.json()
        except Exception:
            body = resp.text
        attach_response(resp.status_code, dict(resp.headers), body, elapsed_ms)


        self.logger.info("API call finished",
                         extra=dict(status=resp.status_code, method=method, client_url=url, elapsed_ms=elapsed_ms))

        if expected_status is not None:
            assert resp.status_code == expected_status, f"Expected {expected_status}, got {resp.status_code}. Body: {resp.text}"

        return resp

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("POST", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("DELETE", endpoint, **kwargs)
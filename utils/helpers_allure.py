import json
import allure

def _attach_json(name: str, data: dict | list | None):
    if data is None:
        allure.attach("—", name=name, attachment_type=allure.attachment_type.TEXT)
        return
    try:
        body = json.dumps(data, ensure_ascii=False, indent=2)
        allure.attach(body, name=name, attachment_type=allure.attachment_type.JSON)
    except Exception:
        allure.attach(str(data), name=name, attachment_type=allure.attachment_type.TEXT)

def attach_request(method: str, url: str, headers: dict | None, params: dict | None, json_body: dict | list | None):
    allure.attach(f"""{method} {url}

Headers: {headers or {}}
Params: {params or {}}""".strip(),
                  name="Request: meta", attachment_type=allure.attachment_type.TEXT)
    _attach_json("Request: body", json_body)

def attach_response(status_code: int, headers: dict | None, json_body: dict | list | str | None, elapsed_ms: int):
    allure.attach(f"Status: {status_code}\nElapsed: {elapsed_ms} ms\nHeaders: {headers or {}}",
                  name="Response: meta", attachment_type=allure.attachment_type.TEXT)
    if isinstance(json_body, (dict, list)):
        _attach_json("Response: body", json_body)
    else:
        allure.attach(str(json_body), name="Response: body", attachment_type=allure.attachment_type.TEXT)
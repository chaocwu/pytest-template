import json

import allure
import requests
from loguru import logger
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from utils.config import GitCodeConfig


class GitCodeAPI:
    def __init__(self, config: GitCodeConfig) -> None:
        self.base_url = config.base_url
        self.headers = {"Authorization": f"Bearer {config.access_token}"}
        self.timeout = 10
        self.session = requests.Session()

        retry = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "DELETE"],
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retry))
        self.session.mount("http://", HTTPAdapter(max_retries=retry))

    def get(self, endpoint: str, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)

    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        prefix = f"[{method}] {url}"

        response = self.session.request(
            method=method,
            url=url,
            headers=self.headers,
            timeout=self.timeout,
            **kwargs,
        )

        logger.info(f"{prefix} status_code: {response.status_code}")

        attachement = {
            "name": prefix,
            "status_code": response.status_code,
            "request": None,
            "reponse": None,
        }

        if "json" in kwargs:
            attachement["request"] = kwargs["json"]
        elif "data" in kwargs:
            attachement["request"] = kwargs["data"]

        try:
            data = response.json()
            attachement["reponse"] = data
            allure.attach(
                json.dumps(attachement, indent=4),
                name=attachement["name"],
                attachment_type=allure.attachment_type.JSON,
            )
            return data
        except json.JSONDecodeError as e:
            logger.warning(f"{prefix} JSON parse error: {e}")
            attachement["reponse"] = response.text
            allure.attach(
                json.dumps(attachement, indent=4),
                name=attachement["name"],
                attachment_type=allure.attachment_type.JSON,
            )
        return response

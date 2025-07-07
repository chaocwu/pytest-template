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

        if "json" in kwargs:
            allure.attach(
                json.dumps(kwargs["json"], indent=4),
                name=f"{method} {url} - Request Body",
                attachment_type=allure.attachment_type.JSON,
            )
        elif "data" in kwargs:
            allure.attach(
                str(kwargs["data"]),
                name=f"{method} {url} - Request Body",
                attachment_type=allure.attachment_type.TEXT,
            )

        try:
            data = response.json()
            allure.attach(
                json.dumps(data, indent=4),
                name=f"{prefix} - Response Body",
                attachment_type=allure.attachment_type.JSON,
            )
            return data
        except json.JSONDecodeError as e:
            logger.warning(f"{prefix} JSON parse error: {e}")
            allure.attach(
                response.text,
                name=f"{prefix} - Response Body",
                attachment_type=allure.attachment_type.TEXT,
            )
        return response

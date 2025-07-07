import json

import allure
import requests
from loguru import logger
from pydantic import BaseModel


class Env(BaseModel):
    base_url: str
    token: str


class IssuesAPI:
    def __init__(self, env: Env) -> None:
        self.env = env

    @allure.step("get jsonplaceholder posts list")
    def get_user_repos(self) -> list[dict]:
        url = f"{self.env.base_url}/user/repos"
        response = requests.get(url)
        assert response.status_code == 200, f"status code is {response.status_code}"
        data = response.json()
        logger.info(data)
        allure.attach(json.dumps(response), allure.attachment_type.JSON)
        return data


class PostsLogic: ...


class PostsValidator:
    @allure.step("check posts list")
    @staticmethod
    def check_posts_list(data: list) -> bool:
        return isinstance(data, list) and len(data) > 0

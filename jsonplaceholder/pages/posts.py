import allure
import requests
from loguru import logger

URL = "https://jsonplaceholder.typicode.com/posts"


class PostsAPI:
    def __init__(self, user) -> None:
        self.user = user

    @allure.step("get jsonplaceholder posts list")
    def get_posts(self) -> list[dict]:
        response = requests.get(URL).json()
        logger.info(response)
        allure.attach(response, allure.attachment_type.JSON)
        return response

    @allure.step("get jsonplaceholder post by id")
    def get_post_by_id(self, id: int) -> dict:
        response = requests.get(URL + f"/{id}").json()
        logger.info(response)
        allure.attach(response, allure.attachment_type.JSON)
        return response


class PostsLogic:
    def __init__(self, posts: PostsAPI) -> None:
        self.posts = posts

    @allure.step("posts list")
    def list_posts(self):
        return self.posts.get_posts()


class PostsValidator:
    @allure.step("check posts list")
    @staticmethod
    def check_posts_list(data: list) -> bool:
        return isinstance(data, list) and len(data) > 0

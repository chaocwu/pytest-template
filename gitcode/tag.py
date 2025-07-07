from dataclasses import asdict, dataclass

import allure
from requests import Response

from utils.api import GitCodeAPI


@dataclass
class Tag:
    tag_name: str
    tag_message: str
    refs: str = "main"


@dataclass
class TagPathParams:
    owner: str
    repo: str
    tag_name: str = ""


class TagAPI(GitCodeAPI):
    @allure.step("List all tags for repo")
    def list_repo_tags(self, params: TagPathParams) -> list:
        url = f"/repos/{params.owner}/{params.repo}/tags"
        response = self.get(url)
        assert isinstance(response, list), "Expected a list of tags"
        return response

    @allure.step("Create a personal project repository")
    def create_repo_tag(self, params: TagPathParams, data: Tag):
        url = f"/repos/{params.owner}/{params.repo}/tags"
        response = self.post(url, json=asdict(data))
        assert isinstance(response, dict), "Expected a dictionary response"
        return response

    @allure.step("Delete a repository")
    def delete_repo_tag(self, params: TagPathParams):
        url = f"/repos/{params.owner}/{params.repo}/tags/{params.tag_name}"
        response = self.delete(url)
        assert isinstance(response, Response), "Expected a dictionary response"
        return response

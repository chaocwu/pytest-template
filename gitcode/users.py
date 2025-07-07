from dataclasses import asdict, dataclass

import allure
from requests import Response

from utils.api import GitCodeAPI


@dataclass
class Repo:
    name: str
    gitignore_template: str = "JavaScript"
    license_template: str = "MulanPSL-2.0"


@dataclass
class RepoPathParams:
    owner: str
    repo: str


class ReposAPI(GitCodeAPI):
    @allure.step("List all repositories for authorized users")
    def list_user_repos(self) -> list:
        response = self.get("/user/repos")
        assert isinstance(response, list), "Expected a list of repositories"
        return response

    @allure.step("Create a personal project repository")
    def create_user_repo(self, data: Repo):
        response = self.post("/user/repos", json=asdict(data))
        assert isinstance(response, dict), "Expected a dictionary response"
        return response

    @allure.step("Delete a repository")
    def delete_repo(self, params: RepoPathParams):
        response = self.delete(f"/repos/{params.owner}/{params.repo}")
        assert isinstance(response, Response), "Expected a dictionary response"
        return response

    @allure.step("Get a user's repository")
    def get_repo(self, params: RepoPathParams):
        response = self.get(f"/repos/{params.owner}/{params.repo}")
        assert isinstance(response, dict), "Expected a dictionary response"
        return response


class IssuesLogic: ...


class IssuesValidator: ...

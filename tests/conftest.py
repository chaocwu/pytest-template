import os
import time

import allure
import pytest
from loguru import logger

from gitcode.users import Repo, RepoPathParams, ReposAPI
from utils.config import GitCodeConfig


@pytest.fixture(scope="session")
def config():
    base_url = os.getenv("GITCODE_BASE_URL")
    owner = os.getenv("GITCODE_PERSONAL_OWNER")
    token = os.getenv("GITCODE_PERSONAL_ACCESS_TOKEN")
    logger.info(f"Env vars: {base_url}, {owner}, {token}")
    assert base_url and owner and token, "environment variables must be set."
    conf = GitCodeConfig(
        base_url=base_url,
        owner=owner,
        access_token=token,
    )
    logger.info(conf)
    return conf


@pytest.fixture(scope="function")
@allure.title("Prepare for the test basic repo")
def repo(config):
    repo_name = str(time.time_ns() // 1000000)

    repos = ReposAPI(config)
    params = RepoPathParams(
        owner="chaocw",
        repo=repo_name,
    )
    with allure.step("ensure repo is non-existing"):
        repo = repos.get_repo(params)
        status = repo.get("error_code")
        assert isinstance(status, int) and status == 404, status

    with allure.step("create a repo by timestamp"):
        repo = Repo(name=repo_name)
        response = repos.create_user_repo(repo)
        name = response.get("name")
        assert name == repo_name, name

    yield repo_name

    with allure.step("ensure repo is existing"):
        repo = repos.get_repo(params)
        name = response.get("name")
        assert name == repo_name, name

    with allure.step("delete a repo by timestamp"):
        response = repos.delete_repo(params)
        assert response.status_code == 204, response.status_code

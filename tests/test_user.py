import allure

from gitcode.users import RepoPathParams, ReposAPI


@allure.suite("Users")
@allure.label("owner", "chaocw")
@allure.tag("API", "SM")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Query for non-existing personal repository")
def test_query_non_exist_personal_repo(config):
    repos = ReposAPI(config)
    repo_path_params = RepoPathParams(
        owner=config.owner,
        repo="xxx",
    )
    with allure.step("Error code 404 was returned"):
        response = repos.get_repo(repo_path_params)
        error_code = response.get("error_code")
        assert isinstance(error_code, int) and error_code == 404, error_code

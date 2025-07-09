import allure

from gitcode.tag import Tag, TagAPI, TagPathParams


@allure.suite("Tag")
@allure.label("owner", "chaocw")
@allure.tag("API")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create a tag under repo")
def test_create_tag_under_repo(config, repo):
    tag = TagAPI(config)
    data = Tag(tag_name="v1.0.0", tag_message="version 1.0")
    params = TagPathParams(config.owner, repo)
    with allure.step("list tags ensure non-existing current tag"):
        response = tag.list_repo_tags(params)
        if len(response) > 0:
            for item in response:
                assert data.tag_name != item.get("name"), item
    with allure.step("create tag under repo"):
        response = tag.create_repo_tag(params, data)
        assert response.get("name") == data.tag_name, response
    with allure.step("check tag name and message"):
        response = tag.list_repo_tags(params)
        assert len(response) == 0, response
        for item in response:
            assert isinstance(item, dict), item
            if item.get("name") == data.tag_name:
                message = item.get("message")
                assert isinstance(message, str), message
                index = message.index(data.tag_message)
                assert index == 0, item.get("message")
                break
        else:
            assert False, response

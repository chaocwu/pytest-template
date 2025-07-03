import allure

from jsonplaceholder.posts import PostsAPI, PostsValidator


@allure.title("test jsonplaceholder posts list")
def test_jsonplaceholder_posts():
    posts = PostsAPI(None)

    with allure.step("Get posts list"):
        posts_data = posts.get_posts()

    with allure.step("Check posts list"):
        assert PostsValidator.check_posts_list(posts_data)

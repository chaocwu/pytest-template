import allure
import pytest


def test_passed():
    assert True


@pytest.mark.skip(reason="This test is skipped")
def test_skipped():
    assert True


def test_broken():
    raise Exception("This test is broken")


@allure.title("This is a step failed_fixture")
@pytest.fixture(scope="function")
def setup_failed_fixture():
    raise Exception("This fixture is broken")


@allure.title("This test fixture setup is broken")
def test_failed_fixture_setup(failed_fixture):
    with allure.step("This is a step"):
        assert True


@allure.title("This is a step teardown_fixture")
@pytest.fixture(scope="function")
def teardown_fixture():
    yield True
    raise Exception("This fixture is broken")


@allure.title("This test fixture teardown is broken")
def test_failed_fixture_teardown(teardown_fixture):
    with allure.step("This is a step"):
        assert True
    with allure.step("This is a step"):
        with allure.step("This is a step"):
            assert True
        with allure.step("This is a step"):
            assert teardown_fixture

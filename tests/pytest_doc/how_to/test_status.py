import time

import allure
import pytest


def test_passed():
    time.sleep(1)
    assert True


@pytest.mark.skip(reason="This test is skipped")
def test_skipped():
    time.sleep(2)
    assert True


def test_broken():
    time.sleep(3)
    raise Exception("This test is broken")


@allure.title("This is a step failed_fixture")
@pytest.fixture(scope="function")
def setup_failed_fixture():
    time.sleep(4)
    raise Exception("This fixture is broken")


@allure.title("This test fixture setup is broken")
def test_failed_fixture_setup(failed_fixture):
    with allure.step("This is a step"):
        time.sleep(5)
        assert failed_fixture


@allure.title("This is a step teardown_fixture")
@pytest.fixture(scope="function")
def teardown_fixture():
    time.sleep(6)
    yield True
    raise Exception("This fixture is broken")


@allure.title("This test fixture teardown is broken")
def test_failed_fixture_teardown(teardown_fixture):
    with allure.step("This is a step1"):
        time.sleep(7)
        assert True
    with allure.step("This is a step2"):
        with allure.step("This is a step3"):
            time.sleep(8)
            assert True
        with allure.step("This is a step4"):
            time.sleep(9)
            assert teardown_fixture

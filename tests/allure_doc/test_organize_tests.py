import allure
import pytest


@pytest.fixture(scope="module")
def organize_tests():
    return ["Packages", "Suites", "Behaviors"]


@allure.title("Test Packages-based hierarchy")
def test_packages_based_hierarchy(organize_tests):
    assert organize_tests[0] == "Packages", "Navigation method should be 'Packages'"


@allure.parent_suite("Tests for parent_suite")
@allure.suite("Tests for suite")
@allure.sub_suite("Tests for sub_suite")
@allure.title("Test Suite-based hierarchy")
def test_suite_based_hierarchy(organize_tests):
    assert organize_tests[1] == "Suites", "Navigation method should be 'Suites'"


@allure.epic("Tests for epic")
@allure.feature("Tests for feature")
@allure.story("Tests for story")
@allure.title("Test Behavior-based hierarchy")
def test_behavior_based_hierarchy(organize_tests):
    assert organize_tests[2] == "Behaviors", "Navigation method should be 'Behaviors'"

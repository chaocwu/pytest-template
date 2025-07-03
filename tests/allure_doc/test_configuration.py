"""python -m pytest --alluredir allure-results --clean-alluredir"""

import allure
import pytest


@pytest.fixture(scope="module")
def options_affecting_results_collection():
    return [
        "--alluredir ⟨DIRECTORY⟩",
        "--clean-alluredir",
        "--allure-no-capture",
    ]


@pytest.fixture(scope="module")
def options_affecting_test_selection():
    return [
        "--allure-severities ⟨SEVERITY1⟩,⟨SEVERITY2⟩,...",
        "--allure-epics ⟨EPIC1⟩,⟨EPIC2⟩,...",
        "--allure-features ⟨FEATURE1⟩,⟨FEATURE2⟩,...",
        "--allure-stories ⟨STORY1⟩,⟨STORY2⟩,...",
        "--allure-label ⟨LABEL1⟩=⟨VALUE1⟩,⟨LABEL2⟩=⟨VALUE2⟩,...",
    ]


@allure.title("Test Options affecting results collection")
def test_options_affecting_results_collection(options_affecting_results_collection):
    assert len(options_affecting_results_collection) == 3, (
        "There should be 3 options affecting results collection"
    )


@allure.title("Options affecting test selection")
def test_options_affecting_test_selection(options_affecting_test_selection):
    assert len(options_affecting_test_selection) == 5, (
        "There should be 5 options affecting test selection"
    )

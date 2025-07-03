import allure
import pytest


@pytest.fixture(scope="module")
def specifying_which_tests():
    return {
        "Run tests in a module": "pytest test_mod.py",
        "Run tests in a directory": "pytest testing/",
        "Run tests by keyword expressions": "pytest -k 'MyClass and not method'",
        "Run tests by collection arguments": "pytest tests/test_mod.py::TestClass::test_method",
        "Run tests by marker expressions": "pytest -m slow # @pytest.mark.slow",
    }


@allure.title("Test Specifying which tests to run")
def tests_specifying_which_tests_to_run(specifying_which_tests):
    assert len(specifying_which_tests) == 5, (
        "There should be 5 methods of specifying which tests to run"
    )


@allure.title("Test Run tests in a module")
def tests_run_tests_in_a_module(specifying_which_tests):
    assert specifying_which_tests["Run tests in a module"] == "pytest test_mod.py", (
        "Run tests in a module"
    )


@allure.title("Test Run tests in a directory")
def tests_run_tests_in_a_directory(specifying_which_tests):
    assert specifying_which_tests["Run tests in a directory"] == "pytest testing/", (
        "Run tests in a directory"
    )


@allure.title("Test Run tests by keyword expressions")
def tests_run_tests_by_keyword_expressions(specifying_which_tests):
    assert (
        specifying_which_tests["Run tests by keyword expressions"]
        == "pytest -k 'MyClass and not method'"
    ), "Run tests by keyword expressions"


@allure.title("Test Run tests by collection arguments")
def tests_run_tests_by_collection_arguments(specifying_which_tests):
    assert (
        specifying_which_tests["Run tests by collection arguments"]
        == "pytest tests/test_mod.py::TestClass::test_method"
    ), "Run tests by collection arguments"


@allure.title("Test Run tests by marker expressions")
def tests_run_tests_by_marker_expressions(specifying_which_tests):
    assert (
        specifying_which_tests["Run tests by marker expressions"]
        == "pytest -m slow # @pytest.mark.slow"
    ), "Run tests by marker expressions"

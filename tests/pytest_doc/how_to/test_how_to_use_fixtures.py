import allure
import pytest


@pytest.fixture(scope="module")
def how_to_use_fixtures():
    return {
        "Requesting fixtures": [
            "Fixtures can request other fixtures",
            "Fixtures are reusable",
            "A test/fixture can request more than one fixture at a time",
            "Fixtures can be requested more than once per test (return values are cached)",
        ],
        "Autouse fixtures": "We can make a fixture an autouse fixture by passing in autouse=True to the fixture’s decorator. ",
        "Scope": [
            "function: the default scope, the fixture is destroyed at the end of the test.",
            "class: the fixture is destroyed during teardown of the last test in the class.",
            "module: the fixture is destroyed during teardown of the last test in the module.",
            "package: the fixture is destroyed during teardown of the last test in the package where the fixture is defined, including sub-packages and sub-directories within it.",
            "session: the fixture is destroyed at the end of the test session.",
        ],
        "Teardown/Cleanup": [
            "yield fixtures (recommended)",
            "Adding finalizers directly",
        ],
        "Safe fixture structure": "The safest and simplest fixture structure requires limiting fixtures to only making one state-changing action each, and then bundling them together with their teardown code",
        "Using markers to pass data to fixtures": "request.node.get_closest_marker('fixt_data') # @pytest.mark.fixt_data(42)",
        "Overriding fixtures on various levels": [
            "Override a fixture on a folder (conftest) level",
            "Override a fixture on a test module level",
            "Override a fixture with direct test parametrization",
        ],
    }


@allure.title("Test Requesting fixtures")
def tests_requesting_fixtures(how_to_use_fixtures):
    assert len(how_to_use_fixtures["Requesting fixtures"]) == 4, (
        "There should be 4 ways to request fixtures"
    )


@allure.title("Test Autouse fixtures")
def tests_autouse_fixtures(how_to_use_fixtures):
    assert (
        how_to_use_fixtures["Autouse fixtures"]
        == "We can make a fixture an autouse fixture by passing in autouse=True to the fixture’s decorator. "
    )


@allure.title("Test fixtures scope")
def tests_scope_fixtures(how_to_use_fixtures):
    assert len(how_to_use_fixtures["Scope"]) == 5, (
        "There should be 5 scopes for fixtures"
    )


@allure.title("Test fixtures Teardown/Cleanup")
def tests_fixtures_teardown_cleanup(how_to_use_fixtures):
    assert len(how_to_use_fixtures["Teardown/Cleanup"]) == 2, (
        "There should be 2 ways to cleanup fixtures"
    )


@allure.title("Test Safe fixture structure")
def tests_safe_fixture_structure(how_to_use_fixtures):
    assert (
        how_to_use_fixtures["Safe fixture structure"]
        == "The safest and simplest fixture structure requires limiting fixtures to only making one state-changing action each, and then bundling them together with their teardown code"
    )


@allure.title("Test Using markers to pass data to fixtures")
def tests_using_markers_to_pass_data_to_fixtures(how_to_use_fixtures):
    assert (
        how_to_use_fixtures["Using markers to pass data to fixtures"]
        == "request.node.get_closest_marker('fixt_data') # @pytest.mark.fixt_data(42)"
    )


@allure.title("Test Overriding fixtures on various levels")
def tests_overriding_fixtures_on_various_levels(how_to_use_fixtures):
    assert len(how_to_use_fixtures["Overriding fixtures on various levels"]) == 3, (
        "There should be 3 examples"
    )

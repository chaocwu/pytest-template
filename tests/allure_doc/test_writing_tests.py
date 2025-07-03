import allure
import pytest


@pytest.fixture(scope="module")
def organize_tests():
    return ["Packages", "Suites", "Behaviors"]


@pytest.fixture(scope="module")
def writing_tests_steps():
    return [
        "provide description, links and other metadata",
        "organize tests into hierarchies",
        "divide the test into smaller, easier-to-read test steps",
        "describe parameters used when running parametrized tests",
        "add readable titles to fixtures",
        "make the test save screenshots and other files during execution",
        "select which tests to run via a test plan file",
    ]


@pytest.fixture(scope="module")
def tests_metadata():
    return ["description", "tag", "severity", "label", "link", "issue", "testcase"]


@allure.title("Test Specify description, links and other metadata")
@allure.description(
    "This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication."
)
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_specify_metadata(tests_metadata):
    assert len(tests_metadata) == 7, (
        "There should be 7 metadata types specified: description, tag, severity, label, link, issue, and testcase"
    )


@allure.title("Test Packages-based hierarchy")
def test_packages_based_hierarchy(organize_tests):
    assert len(organize_tests) == 3, (
        "There should be 3 methods of organizing tests: Packages, Suites, and Behaviors"
    )


@allure.parent_suite("Tests for parent_suite")
@allure.suite("Tests for suite")
@allure.sub_suite("Tests for sub_suite")
@allure.title("Test Suite-based hierarchy")
def test_suite_based_hierarchy(organize_tests):
    assert len(organize_tests) == 3, (
        "There should be 3 methods of organizing tests: Packages, Suites, and Behaviors"
    )


@allure.epic("Tests for epic")
@allure.feature("Tests for feature")
@allure.story("Tests for story")
@allure.title("Test Behavior-based hierarchy")
def test_behavior_based_hierarchy(organize_tests):
    assert len(organize_tests) == 3, (
        "There should be 3 methods of organizing tests: Packages, Suites, and Behaviors"
    )


@allure.title("Test Divide a test into steps")
def test_divide_test_into_steps():
    with allure.step("Step 1"):
        ...

    with allure.step("Step 2"):
        ...


@pytest.mark.parametrize(
    "param",
    [
        "ui",
        "api",
    ],
)
@allure.title("Test Describe parametrized tests: {param}")
def test_describe_parametrized_tests(param):
    assert param in ["ui", "api"], (
        f"Parametrized test should be either 'ui' or 'api', but got '{param}'"
    )


@pytest.fixture(scope="module")
@allure.title("Prepare for the test")
def describe_fixture():
    ...
    yield "fixture"
    ...


@allure.title("Test Describe fixtures")
def test_describe_fixtures(describe_fixture):
    assert describe_fixture == "fixture", "fixture should be fixture"

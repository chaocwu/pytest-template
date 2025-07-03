import random

import pytest


def test_passed():
    assert True


def test_failed():
    assert random.choice([True, False]), "This test passed or failed randomly"


@pytest.mark.skip(reason="This test is skipped")
def test_skipped():
    assert True


def test_broken():
    raise Exception("This test is broken")


def probabilistic_success(success_rate: float) -> bool:
    return random.random() < success_rate

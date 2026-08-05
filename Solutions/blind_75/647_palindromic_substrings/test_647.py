from problem_647_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("abc", 3),
    ("aaa", 6)
])

def testCountSubstrings(s, expected):
    assert Solution.countSubstrings("", s) == expected
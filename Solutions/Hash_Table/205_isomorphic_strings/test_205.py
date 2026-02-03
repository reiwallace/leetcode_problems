from problem_205_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("s, t, expected", [
    ("egg", "add", True),
    ("f11", "b23", False),
    ("paper", "title", True),
    ("badc", "baba", False)
])

def testIsIsomorphic(s, t, expected):
    assert Solution.isIsomorphic("", s, t) == expected
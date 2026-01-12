from problem_20_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
    ("([)]", False)
])

def testIsValid(s, expected):
    assert Solution.isValid("", s) == expected
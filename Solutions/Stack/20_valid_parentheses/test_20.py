from problem_20_attempt_3 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
    ("([)]", False),
    ("){", False),
    ("))", False)
])

def testIsValid(s, expected):
    assert Solution.isValid("", s) == expected
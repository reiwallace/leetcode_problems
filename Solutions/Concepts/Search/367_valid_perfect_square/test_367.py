from problem_367_revision_1 import Solution
import pytest

@pytest.mark.parametrize("num, expected", [
    (16, True),
    (14, False)
])

def testIsPerfectSquare(num, expected):
    assert Solution.isPerfectSquare("", num) == expected
from problem_278_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("n, bad, expected", [
    (5, 4, 4),
    (1, 1, 1)
])

def testFirstBadVersion(n, bad, expected):
    assert Solution.firstBadVersion("", n, bad) == expected
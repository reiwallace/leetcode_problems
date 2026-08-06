from problem_3345_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("n, t, expected", [
    (10, 2, 10),
    (15, 3, 16)
])

def testSmallestNumber(n, t, expected):
    assert Solution.smallestNumber("", n, t) == expected
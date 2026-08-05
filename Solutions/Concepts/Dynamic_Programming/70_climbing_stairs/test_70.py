from problem_70_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("n, expected", [
    (2, 2),
    (3, 3),
    (1, 1)
])

def testClimbStairs(n, expected):
    assert Solution.climbStairs("", n) == expected
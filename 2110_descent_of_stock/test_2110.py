from problem_2110_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("prices, expected", [
    ([3,2,1,4], 7),
    ([8,6,7,7], 4),
    ([1], 1)
])

def testDescentPeriods(prices, expected):
    assert Solution.getDescentPeriods("", prices) == expected
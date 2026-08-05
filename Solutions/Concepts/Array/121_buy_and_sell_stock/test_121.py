from problem_121_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("prices, expected", [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
    ([2,7,1,4], 5)
])

def testMaxProfit(prices, expected):
    assert Solution.maxProfit("", prices) == expected
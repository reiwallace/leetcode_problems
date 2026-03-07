from problem_575_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("candyType, expected", [
    ([1,1,2,2,3,3], 3),
    ([1,1,2,3], 2),
    ([6,6,6,6], 1)
])

def testDistributeCandies(candyType, expected):
    assert Solution.distributeCandies("", candyType) == expected
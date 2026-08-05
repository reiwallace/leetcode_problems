from problem_15_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]]),
    ([0,0,0,0], [[0,0,0]])
])

def testThreeSum(nums, expected):
    assert Solution.threeSum("", nums) == expected
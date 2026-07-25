from problem_53_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1], 1),
    ([5,4,-1,7,8], 23)
])

def testMaxSubArray(nums, expected):
    assert Solution.maxSubArray("", nums) == expected
from problem_238_attempt_5 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,4], [24,12,8,6]),
    ([-1,1,0,-3,3], [0,0,9,0,0]),
    ([0,0,0], [0,0,0]),
    ([0,2,3,4], [24,0,0,0])
])

def testProductExceptSelf(nums, expected):
    assert Solution.productExceptSelf("", nums) == expected
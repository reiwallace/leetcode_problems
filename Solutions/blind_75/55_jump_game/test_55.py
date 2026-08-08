from problem_55_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False)
])

def testCanJump(nums, expected):
    assert Solution.canJump("", nums) == expected
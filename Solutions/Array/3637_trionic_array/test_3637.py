from problem_3637_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([1,3,5,4,2,6], True),
    ([2,1,3], False),
    ([9,4,6,8], False)
])

def testIsTrionic(nums, expected):
    assert Solution.isTrionic("", nums) == expected
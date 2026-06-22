from problem_268_attempt_3 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([3,0,1], 2),
    ([0,1], 2),
    ([9,6,4,2,3,5,7,0,1], 8)
])

def testMissingNumber(nums, expected):
    assert Solution.missingNumber("", nums) == expected
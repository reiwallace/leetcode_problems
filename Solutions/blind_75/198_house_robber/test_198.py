from problem_198_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,1], 4),
    ([2,7,9,3,1], 12)
])

def testRob(nums, expected):
    assert Solution.rob("", nums) == expected
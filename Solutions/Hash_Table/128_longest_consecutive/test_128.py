from problem_128_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([100,4,200,1,3,2], 4),
    ([0,3,7,2,5,8,4,6,0,1], 9),
    ([1,0,1,2], 3)
])

def testLongestConsecutive(nums, expected):
    assert Solution.longestConsecutive("", nums) == expected
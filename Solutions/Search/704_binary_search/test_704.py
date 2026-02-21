from problem_704_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("nums, target, expected", (
    [[-1,0,3,5,9,12], 9, 4],
    [[-1,0,3,5,9,12], 2, -1]
))

def testSearch(nums, target, expected):
    assert Solution.search("", nums, target) == expected
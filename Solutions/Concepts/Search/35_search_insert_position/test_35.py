from problem_35_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("nums, target, expected", [
    ([1,3,5,6], 5, 2),
    ([1,3,5,6], 2, 1),
    ([1,3,5,6], 7 ,4),
    ([1,3,5,6], 0, 0)
])

def testSearchInsert(nums, target, expected):
    assert Solution.searchInsert("", nums, target) == expected
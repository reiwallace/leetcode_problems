from problem_2176_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("nums, k, expected", [
    ([3,1,2,2,2,1,3], 2, 4),
    ([1,2,3,4], 1, 0),
    ([5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3], 7, 18)
])

def test_equal_divisible_pairs(nums, k, expected):
    assert Solution.countPairs("", nums, k) == expected
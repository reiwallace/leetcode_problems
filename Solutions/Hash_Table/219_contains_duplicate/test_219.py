from problem_219_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("nums, k, expected", [
    ([1,2,3,1], 3, True),
    ([1,0,1,1], 1, True),
    ([1,2,3,1,2,3], 2, False)
])

def testContainsNearbyDuplicate(nums, k, expected):
    assert Solution.containsNearbyDuplicate("", nums, k) == expected
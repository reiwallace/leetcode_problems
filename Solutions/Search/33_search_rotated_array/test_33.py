from problem_33_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("nums, target, expected", [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([1], 0, -1)
])

def testSearch(nums, target, expected):
    assert Solution.search("", nums, target) == expected
from problem_136_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1], 1)
])

def testSingleNumber(nums, expected):
    assert Solution.singleNumber("", nums) == expected
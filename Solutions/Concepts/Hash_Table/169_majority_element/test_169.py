from problem_169_revision import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2),
    ([1], 1),
    ([6,5,5], 5)
])

def testMajorityElement(nums, expected):
    assert Solution.majorityElement("", nums) == expected
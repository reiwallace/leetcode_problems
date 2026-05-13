from problem_169_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2)
])

def testMajorityElement(nums, expected):
    assert Solution.majorityElement("", nums) == expected
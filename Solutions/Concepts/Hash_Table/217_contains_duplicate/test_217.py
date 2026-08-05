from problem_217_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True)
])

def testContainsDuplicate(nums, expected):
    assert Solution.containsDuplicate("", nums) == expected
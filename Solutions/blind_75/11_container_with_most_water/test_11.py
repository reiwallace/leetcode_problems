from problem_11_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("height, expected", [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1)
])

def testMaxArea(height, expected):
    assert Solution.maxArea("", height) == expected
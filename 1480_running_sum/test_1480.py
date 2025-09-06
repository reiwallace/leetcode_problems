from problem_1480_attempt_3 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,4], [1,3,6,10]),
    ([1,1,1,1,1], [1,2,3,4,5]),
    ([3,1,2,10,1], [3,4,6,16,17])
])

def test_running_sum(nums, expected):
    assert Solution.runningSum("", nums) == expected
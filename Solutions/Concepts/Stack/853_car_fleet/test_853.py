from problem_853_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("target, position, speed, expected", [
    (12, [10,8,0,5,3], [2,4,1,1,3], 3),
    (10, [3], [3], 1),
    (100, [0,2,4], [4,2,1], 1)
])

def testCarFleet(target, position, speed, expected):
    assert Solution.carFleet("", target, position, speed) == expected
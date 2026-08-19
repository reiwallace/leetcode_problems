from problem_853_revision_2 import Solution
import pytest

@pytest.mark.parametrize("target, position, speed, expected", [
    (12, [10,8,0,5,3], [2,4,1,1,3], 3),
    (10, [3], [3], 1),
    (100, [0,2,4], [4,2,1], 1),
    (10, [0,2], [1,1], 2),
    (10, [0,4,2], [2,1,3], 1),
    (13, [10,2,5,7,4,6,11], [7,5,10,5,9,4,1], 2)
])

def testCarFleet(target, position, speed, expected):
    assert Solution.carFleet("", target, position, speed) == expected
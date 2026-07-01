from problem_338_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("n, expected", [
    (2, [0,1,1]),
    (5, [0,1,1,2,1,2])
])

def testCountBits(n, expected):
    assert Solution.countBits("", n) == expected
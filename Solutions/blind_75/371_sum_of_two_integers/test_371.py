from problem_371_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (-12, -8, -20)
])

def testGetSum(a, b, expected):
    assert Solution.getSum("", a, b) == expected
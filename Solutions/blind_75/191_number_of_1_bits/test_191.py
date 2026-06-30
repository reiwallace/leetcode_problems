from problem_191_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("n, expected", [
    (11, 3),
    (128, 1),
    (2147483645, 30)
])

def testHammingWeight(n, expected):
    assert Solution.hammingWeight("", n) == expected
from problem_38_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("n, expected", [
    (4, "1211"),
    (1, "1")
])

def testCountAndSay(n, expected):
    assert Solution.countAndSay("", n) == expected
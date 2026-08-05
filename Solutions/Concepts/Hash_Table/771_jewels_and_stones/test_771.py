from problem_771_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("jewels, stones, expected", [
    ("aA", "aAAbbbb", 3),
    ("z", "ZZ", 0)
])

def testNumJewelsInStones(jewels, stones, expected):
    assert Solution.numJewelsInStones("", jewels, stones) == expected
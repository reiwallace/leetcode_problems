from problem_605_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("flowerbed, n, expected", [
    ([1,0,0,0,1], 1, True),
    ([1,0,0,0,1], 2, False),
    ([1,0,0,0,0,1], 2, False),
    ([0,0,1,0,1], 1, True),
    ([0,0,0,0,0], 4, False)
])

def testCanPlaceFlowers(flowerbed, n, expected):
    assert Solution.canPlaceFlowers("", flowerbed, n) == expected
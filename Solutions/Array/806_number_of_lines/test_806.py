from problem_806_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("widths, s, expected", [
    ([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],   "abcdefghijklmnopqrstuvwxyz", [3,60]),
    ([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa", [2,4])
])

def testNumberOfLines(widths, s, expected):
    assert Solution.numberOfLines("", widths, s) == expected
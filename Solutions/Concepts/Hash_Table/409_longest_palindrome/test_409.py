from problem_409_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("abccccdd", 7),
    ("a", 1),
    ("adam", 3)
])

def testLongestPalindrome(s, expected):
    assert Solution.longestPalindrome("", s) == expected
from problem_5_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("babad", "bab"),
    ("cbbd", "bb")
])

def testLongestPalindrome(s, expected):
    assert Solution.longestPalindrome("", s) == expected
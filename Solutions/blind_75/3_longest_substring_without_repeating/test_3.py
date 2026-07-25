from problem_3_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("aab", 2),
    ("ohomm", 3),
    ("bpfbhmipx", 7)
])

def testLengthOfLongestSubstring(s, expected):
    assert Solution.lengthOfLongestSubstring("", s) == expected
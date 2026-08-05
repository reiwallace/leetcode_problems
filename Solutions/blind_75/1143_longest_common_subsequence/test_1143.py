from problem_1143_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("text1, text2, expected", [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0),
    ("ylqpejqbalahwr", "yrkzavgdmdgtqpg", 3)
])

def testLongestCommonSubsequence(text1, text2, expected):
    assert Solution.longestCommonSubsequence("", text1, text2) == expected
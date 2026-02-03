from problem_1544_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("leEeetcode", "leetcode"),
    ("abBAcC", ""),
    ("s", "s"),
    ("mC", "mC"),
    ("Pp", "")
])

def testMakeGood(s, expected):
    assert Solution.makeGood("", s) == expected
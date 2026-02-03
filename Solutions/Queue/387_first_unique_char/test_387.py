from problem_387_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
    ("aadadaad", -1)
])

def testFirstUniqChar(s, expected):
    assert Solution.firstUniqChar("", s) == expected
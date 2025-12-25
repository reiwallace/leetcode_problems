from problem_383_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("ransomNote, magazine, expected", [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
    ("aab", "baa", True)
])

def test_can_construct(ransomNote, magazine, expected):
    assert Solution.canConstruct("", ransomNote, magazine) == expected
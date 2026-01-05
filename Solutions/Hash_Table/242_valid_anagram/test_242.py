from problem_242_optimal import Solution
import pytest

@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False)
])

def testIsAnagram(s, t, expected):
    assert Solution.isAnagram("", s, t) == expected
from problem_290_optimal import Solution
import pytest

@pytest.mark.parametrize("pattern, s, expected", [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),
    ("abba", "dog dog dog dog", False),
    ("abc", "b c a", True),
    ("aaa", "aa aa aa aa", False),
    ("jquery", "jquery", False)
])

def testWordPattern(pattern, s, expected):
    assert Solution.wordPattern("", pattern, s) == expected

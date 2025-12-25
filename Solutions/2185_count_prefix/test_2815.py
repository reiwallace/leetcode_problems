from problem_2815_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("words, pref, expected", [
    (["pay","attention","practice","attend"], "at", 2),
    (["leetcode","win","loops","success"], "code", 0)
])

def test_prefix_count(words, pref, expected):
    assert Solution.prefixCount("", words, pref) == expected

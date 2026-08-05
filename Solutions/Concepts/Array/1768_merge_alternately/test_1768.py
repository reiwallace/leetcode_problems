from problem_1768_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("word1, word2, expected", [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd")
])

def testMergeAlternately(word1, word2, expected):
    assert Solution.mergeAlternately("", word1, word2) == expected
from problem_500_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("words, expected", [
    (["Hello","Alaska","Dad","Peace"], ["Alaska","Dad"]),
    (["omk"], []),
    (["adsdf","sfd"], ["adsdf","sfd"]),
    (["asdfghjkl","qwertyuiop","zxcvbnm"], ["asdfghjkl","qwertyuiop","zxcvbnm"])
])

def testFindWords(words, expected):
    assert Solution.findWords("", words) == expected
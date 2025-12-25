from problem_58_attempt_4 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
    ("Hello World", 5) 
])

def testLengthOfLastWord(s, expected):
    assert Solution.lengthOfLastWord("", s) == expected
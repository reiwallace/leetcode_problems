from problem_13_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994)
])

def testRomanToInt(s, expected):
    assert Solution.romanToInt("", s) == expected
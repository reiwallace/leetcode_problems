from problem_125_attempt_5 import Solution
import pytest

@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    (" ", True),
    ("race a car", False),
    ("ab", False),
    (".,", True),
    ("0P", False)
    
])

def testIsPalindrome(s, expected):
    assert Solution.isPalindrome("", s) == expected
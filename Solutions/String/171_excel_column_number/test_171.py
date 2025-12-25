from problem_171_attempt_3 import Solution
import pytest

@pytest.mark.parametrize("columnTitle, expected", [
    ("A", 1),
    ("AB", 28),
    ("ZY", 701)
])

def testTitleToNumber(columnTitle, expected):
    assert Solution.titleToNumber("", columnTitle) == expected
from problem_6_attempt_3 import Solution
import pytest

@pytest.mark.parametrize("s, numRows, expected", [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A"),
    ("AB", 1, "AB")
])

def testConvert(s, numRows, expected):
    assert Solution.convert("", s, numRows) == expected
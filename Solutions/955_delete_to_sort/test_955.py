from problem_955_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("strs, expected", [
    (["ca","bb","ac"], 1),
    (["xc","yb","za"], 0),
    (["zyx","wvu","tsr"], 3),
    (["xga","xfb","yfa"], 1),
    (["abx","agz","bgc","bfc"], 1)
])

def testMinDeletionSize(strs, expected):
    assert Solution.minDeletionSize("", strs) == expected
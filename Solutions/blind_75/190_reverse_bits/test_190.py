from problem_190_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("n, expected", [
    (43261596, 964176192),
    (2147483644, 1073741822)
])

def testReverseBits(n, expected):
    assert Solution.reverseBits("", n) == expected
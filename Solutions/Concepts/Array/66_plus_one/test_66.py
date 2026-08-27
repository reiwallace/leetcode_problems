from problem_66_attempt_1 import Solution
import pytest

@pytest.mark.paramatrize("digits, expected",
    ([1,2,3], [1,2,4]),
    ([4,3,2,1], [4,3,2,2]),
    ([9], [1,0])
)

def testPlusOne(digits, expected):
    assert Solution.plusOne("", digits) == expected
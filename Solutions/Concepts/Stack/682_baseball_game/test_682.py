from  problem_682_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("operations, expected", [
    (["5","2","C","D","+"], 30),
    (["5","-2","4","C","D","9","+","+"], 27),
    (["1","C"], 0)
])

def testCalPoints(operations, expected):
    assert Solution.calPoints("", operations) == expected
from problem_150_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("tokens, expected", [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)
])

def testEvalRPN(tokens, expected):
    assert Solution.evalRPN("", tokens) == expected
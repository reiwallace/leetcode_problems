from problem_509_attempt_2 import Solution
import pytest

@pytest.mark.parametrize("n, expected", [
    (2, 1),
    (3, 2),
    (4, 3)
])

def testFib(n, expected):
    assert Solution.fib("", n) == expected
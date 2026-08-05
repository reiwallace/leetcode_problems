from problem_3310_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("n, k, invocations, expected", [
    (4, 1, [[1,2],[0,1],[3,2]], [0,1,2,3]),
    (5, 0, [[1,2],[0,2],[0,1],[3,4]], [3,4]),
    (3, 2, [[1,2],[0,1],[2,0]], [])
])

def testRemainingMethods(n, k, invocations, expected):
    assert Solution.remainingMethods("", n, k, invocations) == expected
from problem_39_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("candidates, target, expected", [
    ([2,3,6,7], 7, [[2,2,3],[7]]),
    ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
    ([2], 1, [])
])

def testCombinationSum(candidates, target, expected):
    assert Solution.combinationSum("", candidates, target) == expected
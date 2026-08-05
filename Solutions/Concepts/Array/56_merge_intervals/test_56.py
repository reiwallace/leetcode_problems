from problem_56_optimal import Solution
import pytest

@pytest.mark.parametrize("intervals, expected", [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
    ([[4,7],[1,4]], [[1,7]])
])

def testMerge(intervals, expected):
    assert Solution.merge("", intervals) == expected
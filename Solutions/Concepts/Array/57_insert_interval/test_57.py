from problem_57_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("intervals, newInterval, expected", [
    ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]])
])

def testInsert(intervals, newInterval, expected):
    assert Solution.insert("", intervals, newInterval) == expected
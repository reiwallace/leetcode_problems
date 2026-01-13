from problem_739_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("temperatures, expected", [
    ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
    ([30,40,50,60], [1,1,1,0]),
    ([30,60,90], [1,1,0])
])

def testDailyTemperatures(temperatures, expected):
    assert Solution.dailyTemperatures("", temperatures) == expected
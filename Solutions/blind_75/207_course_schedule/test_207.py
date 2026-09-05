from problem_207_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("numcourses, prerequisites, expected", [
    (2, [[1,0]], True),
    (2, [[1,0],[0,1]], True),
    (6, [[1,0],[1,2],[3,1],[3,2],[2,4],[4,5],[2,5]], True)
])

def testCanFinish(numCourses, prerequisites, expected):
    assert Solution.canFinish("", numCourses, prerequisites) == expected
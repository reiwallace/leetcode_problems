from problem_912_attempt_3 import Solution
import pytest

@pytest.mark.parametrize("nums, expected", [
    ([5,2,3,1], [1,2,3,5]),
    ([5,1,1,2,0,0], [0,0,1,1,2,5]),
    ([-4,0,7,4,9,-5,-1,0,-7,-1], [-7,-5,-4,-1,-1,0,0,4,7,9])
])

def testSortArray(nums, expected):
    sol = Solution()
    assert sol.sortArray(nums) == expected
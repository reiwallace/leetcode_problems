from problem_200_attempt_1 import Solution
import pytest

@pytest.mark.parametrize("grid, expected", [
    ([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
], 1),
    ([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
], 3)
])

def testNumIslands(grid, expected):
    assert Solution.numIslands("", grid) == expected
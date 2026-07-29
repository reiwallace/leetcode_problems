from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def markNearby(grid, x, y):
            if grid[x][y] != "1": return

            grid[x][y] = None
            if x + 1 < len(grid):
                markNearby(grid, x + 1, y)
            if y + 1 < len(grid[x]):
                markNearby(grid, x, y + 1)
            if x - 1 >= 0:
                markNearby(grid, x - 1, y)
            if y - 1 >= 0:
                markNearby(grid, x, y - 1)


        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    markNearby(grid, x, y)
                    count += 1
        return count


            
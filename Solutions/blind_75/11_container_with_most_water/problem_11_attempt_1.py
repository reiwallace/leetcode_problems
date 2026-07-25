from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        for i in range(len(height)):
            for x in range(i + 1, len(height)):
                maxWater = max(min(height[x], height[i]) * (x - i), maxWater)
        return maxWater 
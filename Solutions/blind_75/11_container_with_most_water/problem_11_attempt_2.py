from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0
        while left < right:
            maxWater = max(min(height[left], height[right]) * (right - left), maxWater)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxWater
    
    
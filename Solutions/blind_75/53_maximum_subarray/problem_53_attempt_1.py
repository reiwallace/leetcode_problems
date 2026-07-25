from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        previous = 0
        largest = nums[0]
        for num in nums:
            if previous + num > num:
                previous += num
            else:
                previous = num
            largest = max(largest, previous)
        return largest
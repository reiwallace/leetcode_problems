from typing import List

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        compare = len(nums)
        for i in range(len(nums)):
            compare += i
            num += nums[i]

        return compare - num
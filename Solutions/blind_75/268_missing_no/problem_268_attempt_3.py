from typing import List

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        compare = len(nums) * (len(nums) + 1) // 2
        for num in nums:
            compare -= num

        return compare
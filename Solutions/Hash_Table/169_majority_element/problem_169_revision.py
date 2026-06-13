from typing import List

"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        table = {}
        maxCount = len(nums) // 2
        for i in nums:
            if not i in table:
                table[i] = 1
            else:
                table[i] += 1
                if table[i] > maxCount:
                    return i
        return nums[0]
"""

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        candidate = [nums[0], 1]
        for i in range(1, len(nums)):
            if nums[i] == candidate[0]:
                candidate[1] += 1
            else:
                candidate[1] -= 1
                if candidate[1] < 1:
                    candidate[0] = nums[i]
                    candidate[1] = 1
        return candidate[0]
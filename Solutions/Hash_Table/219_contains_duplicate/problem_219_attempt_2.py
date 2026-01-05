from typing import List

class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i in range(len(nums)):
            if nums[i] in table and i - table[nums[i]] <= k: return True
            else: table[nums[i]] = i
        return False
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i in range(len(nums)):
            if not nums[i] in table:
                table[nums[i]] = i
            elif abs(table[nums[i]] - i) <= k:
                return True
            else:
                table[nums[i]] = i

        return False
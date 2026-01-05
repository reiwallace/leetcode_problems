from typing import List

class Solution:
    # Time Complexity O(nm), Space Complexity O(m)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: return False
        nearby = [None] * k
        i = 0
        for n in nums:
            if nearby.count(n) >= 1: return True
            nearby[i] = n
            i += 1
            if i >= k: i = 0
        return False

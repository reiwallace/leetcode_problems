from typing import List

class Solution:
    # Time O(n), Space O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for num in nums:
            if num in table: return True # O(1)
            else: table[num] = 1 # O(1)
        return False
    
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = {}
        for num in nums:
            if not num in table:
                table[num] = 1
            else:
                del table[num]
        for val in table:
            return val

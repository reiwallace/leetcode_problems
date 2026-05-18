from collections import defaultdict
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = {}
        ans = 0

        for num in nums:
            table[num] = 0

        for key in table:
            length = 0

            while key + length in table:
                length += 1

            if length > ans:
                ans = length

        return ans
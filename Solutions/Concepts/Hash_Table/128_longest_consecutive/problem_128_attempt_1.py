from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = {}
        largest = 0
        for num in nums:
            if num in table:
                continue
            l = table.get(num - 1, 0)
            r = table.get(num + 1, 0)
            table[num] = l + r + 1
            table[num - l] = table[num]
            table[num + r] = table[num]
            if largest < table[num]: largest = table[num]

        return largest
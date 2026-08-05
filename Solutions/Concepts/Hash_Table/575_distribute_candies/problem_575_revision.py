from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        table = {}
        for i in candyType:
            if not i in table:
                table[i] = 1
        return min(len(table), len(candyType) // 2)
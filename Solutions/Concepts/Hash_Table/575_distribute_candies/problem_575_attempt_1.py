from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        table = {}
        types = 0
        maxTypes = len(candyType) // 2
        for candy in candyType:
            if candy in table:
                continue
            else:
                table[candy] = 1
                types += 1
                if types > maxTypes:
                    return maxTypes

        if len(table) > maxTypes:
            return maxTypes
        else:
            return len(table)
        

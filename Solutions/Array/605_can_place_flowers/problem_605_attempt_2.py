from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        emptyChain = 1
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                emptyChain = 0
            else:
                emptyChain += 1

            if emptyChain == 3:
                n -= 1
                emptyChain = 1
                if n <= 0:
                    return True 
        if emptyChain == 2 and n == 1:
            return True
        return False 
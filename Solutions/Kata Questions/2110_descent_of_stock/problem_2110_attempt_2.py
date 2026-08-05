from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        descentPeriods = 0
        descentStreak = 0
        priceLen = len(prices)
        for i in range(priceLen):
            if i == 0: continue
            if prices[i - 1] - prices[i] == 1:
                descentStreak += 1
                descentPeriods += descentStreak
            else:
                descentStreak = 0
                
        descentPeriods += priceLen
        return descentPeriods
    
from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        descentPeriods = 0
        for i in range(len(prices)):
            if i == 0: continue
            if prices[i - 1] - prices[i] == 1:
                descentPeriods += 1
                backtrack = 1
                while prices[i - backtrack - 1] - prices[i - backtrack] == 1:
                    if i - backtrack - 1 < 0: break
                    descentPeriods += 1
                    backtrack += 1
        descentPeriods += len(prices)
        return descentPeriods
    
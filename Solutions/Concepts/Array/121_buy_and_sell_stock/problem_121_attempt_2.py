from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pricesLen = len(prices)
        sell = pricesLen - 1
        buy = 0
        n = pricesLen - 1
        for i in range(pricesLen):
            if i < sell and prices[buy] > prices[i]:
                buy = i
            if n > buy and prices[sell] < prices[n]:
                sell = n
            n -= 1
        if prices[sell] - prices[buy] < 0: return 0
        return prices[sell] - prices[buy]


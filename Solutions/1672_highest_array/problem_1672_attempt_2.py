from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            running_total = 0
            for balance in account:
                running_total += balance
            max_wealth = running_total if running_total > max_wealth else max_wealth
        return max_wealth
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for account in range(len(accounts)):
            accounts[account] = sum(accounts[account])
        accounts.sort()
        return accounts[-1]
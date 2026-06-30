from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        memo1 = 0
        memo2 = 0
        for num in nums:
            temp = memo1
            memo1 = max(memo2 + num, memo1)
            memo2 = temp
        return memo1
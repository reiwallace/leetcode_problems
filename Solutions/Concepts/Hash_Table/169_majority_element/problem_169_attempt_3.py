from collections import defaultdict
from typing import List

class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def majorityElement(self, nums: List[int]) -> int:
        table = defaultdict(int)
        for num in nums:
                table[num] += 1

        n = len(nums) // 2
        for num in table:
            if table[num] > n:
                return num
        
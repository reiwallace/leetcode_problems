from typing import List

class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def majorityElement(self, nums: List[int]) -> int:
        table = {}
        greatest = nums[0]
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        for num in table:
            if table[num] > table[greatest]:
                greatest = num
                if table[num] > len(nums) / 2:
                    return greatest

        return greatest
        
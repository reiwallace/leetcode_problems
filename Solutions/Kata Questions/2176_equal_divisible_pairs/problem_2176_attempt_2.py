from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        matching_pairs = 0
        nums_len = len(nums)
        # Check each index in nums
        for first_index in range(nums_len):
            # Only check index's higher than the first index
            for second_index in range(first_index + 1, nums_len):
                if nums[first_index] == nums[second_index] and (first_index * second_index) % k == 0:
                    matching_pairs += 1
        return matching_pairs
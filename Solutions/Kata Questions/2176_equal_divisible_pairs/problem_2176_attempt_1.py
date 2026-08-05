from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Count index's where the values are equal
        matching_pairs = 0
        for first_index in range(len(nums)):
            for second_index in range(len(nums)):
                if second_index <= first_index: 
                    continue
                if nums[first_index] == nums[second_index] and (first_index * second_index) % k == 0:
                    matching_pairs += 1
        return matching_pairs
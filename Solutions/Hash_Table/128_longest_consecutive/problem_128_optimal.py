from typing import List

class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            # Only checks num if it is the start of a sequence
            if n - 1 not in num_set:
                length = 1

                # Count the sequence
                while n + length in num_set:
                    length += 1
                
                longest = max(longest, length)
        
        return longest
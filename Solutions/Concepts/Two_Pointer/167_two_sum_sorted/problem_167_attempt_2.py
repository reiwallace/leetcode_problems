from typing import List
# Brute Force 2
class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for x in range(i + 1, len(numbers)):
                if numbers[i] + numbers[x] == target:
                    return [i + 1, x + 1]

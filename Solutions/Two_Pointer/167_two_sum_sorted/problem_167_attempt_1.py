from typing import List
# Brute Force
class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for x in range(len(numbers) - 1, 0, -1):
                if numbers[i] + numbers[x] == target:
                    return [i + 1, x + 1]

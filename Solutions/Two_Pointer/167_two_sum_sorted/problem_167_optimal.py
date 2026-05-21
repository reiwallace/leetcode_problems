from typing import List

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while True:
            check = numbers[left] + numbers[right]
            if check > target:
                right -= 1
            elif check < target:
                left += 1
            else:
                return [left + 1, right + 1]

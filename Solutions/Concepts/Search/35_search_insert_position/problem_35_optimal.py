from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        bounds = [0, len(nums) - 1]
        while bounds[0] <= bounds[1]:
            mid = (bounds[0] + bounds[1]) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                bounds[0] = mid + 1
            elif nums[mid] > target:
                bounds[1] = mid - 1
            return bounds[0]
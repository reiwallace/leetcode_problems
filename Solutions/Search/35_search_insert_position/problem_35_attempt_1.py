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
        if nums[bounds[1]] < target:
            return bounds[0]
        elif bounds[1] < 0:
            return 0
        else:
            return bounds[1]
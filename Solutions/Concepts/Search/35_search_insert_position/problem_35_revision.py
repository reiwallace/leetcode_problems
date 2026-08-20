from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        upper = len(nums) - 1
        lower = 0
        while lower <= upper:
            mid = (upper + lower) // 2
            midNum = nums[mid]
            if midNum == target:
                return mid
            elif midNum < target:
                lower = mid + 1
            elif midNum > target:
                upper = mid - 1
        return lower
            
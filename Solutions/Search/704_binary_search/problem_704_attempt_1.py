import math
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rang = [0, len(nums) - 1]
        while rang[0] <= rang[1]:
            mid = math.floor(rang[0] + (rang[1] - rang[0]) / 2)
            if nums[mid] > target:
                rang[1] = mid - 1
            elif nums[mid] < target:
                rang[0] = mid + 1
            elif nums[mid] == target:
                return mid
        return -1



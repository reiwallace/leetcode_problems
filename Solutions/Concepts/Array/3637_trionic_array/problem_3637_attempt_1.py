from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        increasing = True
        decreased = False
        previous = nums[0] - 1
        skipNext = False
        for num in nums:
            if skipNext:
                previous = num
                skipNext = False
                continue
            if num < previous and increasing and not decreased:
                increasing = False
                decreased = True
                skipNext = True
            elif num < previous and increasing and decreased:
                return False
            elif num > previous and not increasing:
                increasing = True
                skipNext = True
            previous = num

        return increasing and decreased
            
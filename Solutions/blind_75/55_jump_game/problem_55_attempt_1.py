from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxStep = nums[0]
        curIdx = 0
        while maxStep < len(nums) - 1:
            original = maxStep
            tempIdx = curIdx
            for i in range(nums[curIdx], 0, -1):
                target = curIdx + i
                maxFromTarget = target + nums[target]
                if maxStep < maxFromTarget:
                    maxStep = maxFromTarget
                    tempIdx = target
                
            if maxStep == original:
                return False
            curIdx = tempIdx

        return True

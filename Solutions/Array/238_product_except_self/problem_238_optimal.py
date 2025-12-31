from typing import List

class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        front = 1
        back = 1
        answer = [1] * numsLen

        for i in range(1, numsLen):
            front *= nums[i - 1]
            answer[i] *= front

        for i in range(numsLen - 2, -1, -1):
            back *= nums[i + 1]
            answer[i] *= back

        return answer 
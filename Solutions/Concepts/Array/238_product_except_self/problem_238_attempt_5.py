from typing import List

class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        answerFront = [1] * numsLen
        answerBack = [1] * numsLen
        answer = [1] * numsLen

        for i in range(1, numsLen):
            answerFront[i] = answerFront[i - 1] * nums[i - 1]
            answer[i] *= answerFront[i]

        for i in range(numsLen - 2, -1, -1):
            answerBack[i] = answerBack[i + 1] * nums[i + 1]
            answer[i] *= answerBack[i]

        return answer 
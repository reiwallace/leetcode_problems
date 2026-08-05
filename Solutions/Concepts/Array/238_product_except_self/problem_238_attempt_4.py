from typing import List

class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        zeroIndex = -1
        answerFront = [1 for i in range(numsLen)]
        answerBack = [1 for i in range(numsLen)]
        answer = []

        for i in range(0, numsLen):
            if nums[i] == 0 and i == 0:
                zeroIndex = i
                break
            if i == 0:
                continue
    
            if nums[i] == 0: 
                zeroIndex = i
                answerFront[i] = answerFront[i - 1] * nums[i - 1]
                break
            answerFront[i] = answerFront[i - 1] * nums[i - 1]

        for i in range(numsLen - 1, -1, -1):
            if i == numsLen - 1 and nums[i] == 0 and zeroIndex != i:
                return [0 for i in range(len(nums))]
            elif i == numsLen - 1:
                continue
        
            if nums[i] == 0:
                if zeroIndex != i:
                    return [0 for i in range(len(nums))]
                zeroIndex = i 
                answerBack[i] = answerBack[i + 1] * nums[i + 1]
                break
            answerBack[i] = answerBack[i + 1] * nums[i + 1]

        if zeroIndex != -1: 
            answer = [0 for i in range(len(nums))]
            answer[zeroIndex] = answerBack[zeroIndex] * answerFront[zeroIndex]
            return answer

        for i in range(numsLen):
            answer.append(answerFront[i] * answerBack[i])

        return answer 
from typing import List

class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zeroCount = 0
        answer = []

        for n in nums:
            if n == 0: 
                zeroCount += 1
                if zeroCount > 1: return [0 for i in range(len(nums))]
                continue
            totalProduct *= n

        if zeroCount == 1: 
            answer = [0 for i in range(len(nums))]
            answer[nums.index(0)] = totalProduct 
            return answer

        for i in range(len(nums)):
            answer.append(int(totalProduct / nums[i]))

        return answer
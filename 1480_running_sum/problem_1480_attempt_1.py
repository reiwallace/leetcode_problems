from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            section_sum = 0
            for num in range(len(nums[:i + 1])):
                section_sum += nums[num]
            answer.append(section_sum)
        return answer

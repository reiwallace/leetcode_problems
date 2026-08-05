class Solution:
    # O(n^2) Time complexity, O(n) Space Complexity
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)

        for i in range(n):
            total = 1
            for m in range(n):
                if i == m: continue
                total *= nums[m]
            answer.append(total)

        return answer
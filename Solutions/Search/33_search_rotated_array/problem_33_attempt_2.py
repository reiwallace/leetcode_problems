from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = len(nums) // 2
        for i in range(100):
        #while nums[pivot - 1] < nums[pivot]:
            pivot //= 2
            print(pivot)

        print(pivot)
        return 1
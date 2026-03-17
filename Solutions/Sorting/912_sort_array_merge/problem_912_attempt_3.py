from typing import List
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arrayOne, arrayTwo, original):
            pos = 0
            pointer1 = 0
            pointer2 = 0
            while pointer1 < len(arrayOne) and pointer2 < len(arrayTwo):
                if arrayOne[pointer1] > arrayTwo[pointer2]:
                    original[pos] = arrayTwo[pointer2]
                    pointer2 += 1
                else:
                    original[pos] = arrayOne[pointer1]
                    pointer1 += 1
                pos += 1
            
            while pointer1 < len(arrayOne):
                original[pos] = arrayOne[pointer1]
                pointer1 += 1
                pos += 1

            while pointer2 < len(arrayTwo):
                original[pos] = arrayTwo[pointer2]
                pointer2 += 1
                pos += 1
        
            return original
                    

        numsLen = len(nums)
        if numsLen == 1:
            return nums
    
        arrayOne = nums[:numsLen // 2]
        arrayTwo = nums[numsLen // 2:]

        arrayOne = self.sortArray(arrayOne)
        arrayTwo = self.sortArray(arrayTwo)

        return merge(arrayOne, arrayTwo, nums)
from typing import List

class Solution:
    """
    def bubbleSort(self, nums):
        swaps = 1
        while swaps > 0:
            swaps = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    current = nums[i]
                    nums[i] = nums[i - 1]
                    nums[i - 1] = current
                    swaps += 1
            
            
        return nums
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        divided = [[n] for n in nums]

        while len(divided[0]) < len(nums):
            newArr = []
            if len(divided) % 2 != 0:
                popped = divided.pop()
                divided[-1] += popped
            for i in range(0, len(divided) - 1, 2):
                temp = divided[i] + divided[i + 1]
                
                for i in range(len(temp) / 2):
                    temp2 = []
                    if temp[i] < temp[-i - 1]:
                        temp2.append(temp[i])
                        temp2.append(temp[-i - 1])
                    else:
                        temp2.append(temp[i])
                        temp2.append(temp[-i - 1])


            divided = newArr


        divided[0] = Solution.bubbleSort("", divided[0])
        return divided[0]
    

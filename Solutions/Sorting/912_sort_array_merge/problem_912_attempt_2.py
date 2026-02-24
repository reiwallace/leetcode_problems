from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        divided = [[n] for n in nums]
        while len(divided[0]) < len(nums):
            new_arr = []
            for i in range(0, len(divided), 2):
                if i + 1 > len(divided) - 1:
                    break
                new_arr.append(Solution.mergeSort("", divided[i], divided[i + 1]))
            print("Before", new_arr)
            if len(divided) % 2 != 0 and len(divided) > 1 and len(new_arr) > 1:
                new_arr[-1] = Solution.mergeSort("", new_arr[-1], divided[-1])
            print("Afer", new_arr)
            divided = new_arr
        return divided
    
    def mergeSort(self, arr1, arr2):
        temp = []
        for i in range(max(len(arr1), len(arr2))):
            if i > len(arr1) - 1:
                if arr2[-i - 1] > arr1[len(arr1) - 1]:
                    temp += arr2[:-i]
                    break
                elif arr2[-i - 1] < arr1[len(arr1) - 1]:
                    temp.insert(len(temp) - 2, arr2[-i - 1])
            elif i > len(arr2) - 1:
                if arr2[len(arr2) - 1] > arr1[i]:
                    temp += arr1[i:]
                    break
                elif arr2[len(arr2) - 1] < arr1[len(arr1) - 1]:
                    temp.insert(len(temp) - 2, arr1[i])
            elif arr1[i] > arr2[-i - 1]:
                temp += arr2[:-i]
                temp += arr1[i:]
                break
            elif arr1[i] < arr2[-i - 1]:
                temp.append(arr1[i])
                temp.append(arr2[-i - 1])
        return temp
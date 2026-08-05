from typing import List

class Solution:
    # Time Complexity O(n+m^2), Space Complexity O(n)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Dict = {}
        ans = []
        for n in nums1:
            num1Dict[n] = 1
        
        for n in nums2:
            if n in num1Dict and ans.count(n) == 0:
                ans.append(n)

        return ans
        
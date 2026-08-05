from typing import List

class Solution:
    # Time Complexity O(nm) Space Complexity O(n)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            if ans.count(n) != 0:
                continue
            for m in nums2:
                if n == m and ans.count(n) == 0:
                    ans.append(n)

        return ans
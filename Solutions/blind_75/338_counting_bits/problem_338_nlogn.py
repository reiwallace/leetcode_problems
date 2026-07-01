from typing import List

class Solution:
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(n: int) -> int:
            ans = 0
            while n:
                ans += n & 1
                n >>= 1
            return ans
        
        ans = []
        for i in range(n + 1):
            ans.append(hammingWeight(i))
        return ans
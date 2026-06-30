from typing import List

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        maxBits = 1
        numIndex = 0

        for i in range(n):
            ans.append(1 + ans[numIndex])
            numIndex += 1
            if ans[-1] >= maxBits:
                maxBits += 1
                numIndex = 0

        return ans
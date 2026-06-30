class Solution:
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans += (n >> i) & 1
        return ans
class Solution:
    # Time Complexity O(1)
    # Space Complexity O(1)
    def reverseBits(self, n: int) -> int:
        num = 0
        for i in range(32):
            num += ((n >> (31 - i)) & 1) << i

        return num
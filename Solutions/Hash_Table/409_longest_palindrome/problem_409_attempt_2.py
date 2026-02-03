class Solution:
    # Time Complexity O(n), Space Complexity(n)
    def longestPalindrome(self, s: str) -> int:
        table = {}
        total = 0
        for c in s:
            if c in table:
                total += 2
                del table[c]
            else:
                table[c] = 1

        if table:
            total += 1

        return total 
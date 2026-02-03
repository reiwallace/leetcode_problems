class Solution:
    # Time Complexity O(n), Space Complexity(n)
    def longestPalindrome(self, s: str) -> int:
        table = {}
        for c in s:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1

        oddFound = False
        total = 0
        for n in table:
            if table[n] % 2 == 0:
                total += table[n]
            else:
                if not oddFound:
                    total += 1
                    oddFound = True
                total += table[n] - 1

        return total 
class Solution:
    # O(n) time Complexity, O(1) Space Complexity
    def titleToNumber(self, columnTitle: str) -> int:
        lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        total = 0
        for i in range(len(columnTitle)):
            for n in range(26):
                if lower[n] == columnTitle[-i - 1]: 
                    total += (n + 1) * 26**i
                    break
                if caps[n] == columnTitle[-i - 1]: 
                    total += (n + 1) * 26**i
                    break

        return total
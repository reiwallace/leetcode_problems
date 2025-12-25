class Solution:
    # O(n) time Complexity, O(1) Space Complexity
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        columnTitle = columnTitle.lower()
        for i in range(len(columnTitle)):
            total += (ord(columnTitle[-i - 1]) - 96) * 26**i
        return total
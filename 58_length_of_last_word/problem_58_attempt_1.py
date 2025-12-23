class Solution:
    # Complexity O(n)
    def lengthOfLastWord(self, s: str) -> int:
        split = s.strip().split(" ")
        return len(split[-1])
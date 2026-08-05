class Solution:
    # Time Complexity O(n), Space Complexity O(1)
    def firstUniqChar(self, s: str) -> int:
        char = [0] * 26
        for c in s:
            char[ord(c) - ord("a")] += 1

        for i, c in enumerate(s):
            if char[ord(c) - ord("a")] == 1:
                return i

        return -1
        

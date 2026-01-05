from collections import defaultdict

class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        table = defaultdict(int)
        for c, n in zip(s, t):
            table[c] += 1
            table[n] -= 1
        
        for value in table:
            if table[value] != 0: return False

        return True
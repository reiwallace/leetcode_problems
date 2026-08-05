class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sTable = {}
        tTable = {}
        for c, n in zip(s, t):
            if c in sTable: sTable[c] += 1
            else: sTable[c] = 1
            if n in tTable: tTable[n] += 1
            else: tTable[n] = 1
        return sTable == tTable
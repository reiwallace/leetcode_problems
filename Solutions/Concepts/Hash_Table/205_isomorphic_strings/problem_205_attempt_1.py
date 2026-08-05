class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = {}
        for i in range(len(s)):
            if not s[i] in table:
                table[s[i]] = t[i]
            elif table[s[i]] != t[i]:
                return False
        
        return True
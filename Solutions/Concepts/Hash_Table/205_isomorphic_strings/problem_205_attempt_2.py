class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = {}
        for i in range(len(s)):
            if not s[i] in table:
                if "t" + t[i] in table:
                    return False
                table[s[i]] = t[i]
                table["t" + t[i]] = s[i]
            elif table[s[i]] != t[i]:
                return False
        
        return True

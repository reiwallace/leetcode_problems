class Solution:
    def firstUniqChar(self, s: str) -> int:
        noRepeating = []
        table = {}
        for i in range(len(s)):
            if s[i] in table:
                table[s[i]] += 1
                while noRepeating and table[s[noRepeating[0]]] > 1:
                    noRepeating.popleft()
            else:
                table[s[i]] = 1
                noRepeating.append(i)
        
        if not noRepeating:
            return -1
        return noRepeating[0]
class Solution:
    # Time Complexity O(n), Space Complexity O(n + m)
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = {}
        table2 = {}
        s = s.split()
        if len(s) != len(pattern): return False
        for word, char in zip(s, pattern):
            if char in table and table[char] != word: return False
            table[char] = word
            if word in table2 and table2[word] != char: return False
            table2[word] = char
        return True 
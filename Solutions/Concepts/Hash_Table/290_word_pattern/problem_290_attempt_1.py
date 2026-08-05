class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = {}
        for word, char in zip(s.split(), pattern):
            if char in table and table[char] != word: return False
            table[char] = word
        return True 
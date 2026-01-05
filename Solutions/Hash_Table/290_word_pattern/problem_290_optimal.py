class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = {}
        s = s.split()
        if len(s) != len(pattern): return False
        for word, char in zip(s, pattern):
            word = "w" + word
            char = "c" + char
            if char in table and table[char] != word: return False
            table[char] = word
            if word in table and table[word] != char: return False
            table[word] = char
        return True 
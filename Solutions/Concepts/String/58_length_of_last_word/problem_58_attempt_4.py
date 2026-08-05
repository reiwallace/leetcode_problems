class Solution:
    # O(n) Complexity
    def lengthOfLastWord(self, s: str) -> int:
        sLen = len(s)
    
        # Find index of last non space character
        lastChar = 0
        for char in range(sLen):
            if s[char] != " ":
                lastChar = char
        
        # Count word length - reseting after each space
        wordLength = 0
        for char in range(sLen):
            wordLength += 1
            if s[char] == " ":
                wordLength = 0

            if char == lastChar:
                break
                
        return wordLength

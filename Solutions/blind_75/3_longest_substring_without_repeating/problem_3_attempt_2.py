class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charTable = {}
        startIdx = 0
        maxLen = 0
        for i in range(len(s)):
            char = s[i]
            if char in charTable and charTable[char] >= startIdx:
                maxLen = max(maxLen, i - startIdx)
                startIdx = charTable[char] + 1

            charTable[char] = i

        return max(maxLen, len(s) - startIdx)
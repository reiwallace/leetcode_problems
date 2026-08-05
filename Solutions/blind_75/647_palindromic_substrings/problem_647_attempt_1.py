class Solution:
    def countSubstrings(self, s: str) -> int:
        previousPal = False
        palLength = 0
        palCount = sLen = len(s)
        for i, char in enumerate(s):
            if previousPal:
                if palLength + 2 < sLen and s[i - palLength - 1] == char:
                    palLength += 2
                    palCount += 1
                else:
                    previousPal = False
                    palLength = 0

            if not previousPal:
                if i > 0 and char == s[i - 1]:
                    palLength = 2
                    previousPal += 1
                    palCount += 1
                elif i > 1 and char == s[i - 2]:
                    palLength = 3
                    previousPal += 1
                    palCount += 1

        return palCount
                
                
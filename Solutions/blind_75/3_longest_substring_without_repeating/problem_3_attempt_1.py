class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        startOfSubstring = 0
        endOfSubstring = 0
        maxLength = 0
        curSubString = {}
        for char in s:
            if char in curSubString:
                if len(curSubString) > maxLength:
                    maxLength = len(curSubString)
                i = startOfSubstring
                while s[i] != char and s[i] in curSubString:
                    del curSubString[s[i]]
                    i += 1
                curSubString[char] = 1
                startOfSubstring = endOfSubstring

            else:
                curSubString[char] = 1
            endOfSubstring += 1
        
        print(curSubString)
        if len(curSubString) > maxLength:
            return len(curSubString)
        return maxLength


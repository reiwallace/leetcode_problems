class Solution:
    def isPalindrome(self, s: str) -> bool:
        validChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        n = 0
        m = len(s) - 1

        while n < m:
            while validChars.count(s[n]) < 1 and caps.count(s[n]) < 1 and n < m: n += 1
            while validChars.count(s[m]) < 1 and caps.count(s[m]) < 1 and n < m: m -= 1

            nChar = s[n]
            mChar = s[m]
            if caps.count(nChar) > 0: nChar = validChars[caps.index(nChar)]
            if caps.count(mChar) > 0: mChar = validChars[caps.index(mChar)]
            if nChar != mChar: return False

            n += 1
            m -= 1
            
        return True


class Solution:
    # O(n) Complexity
    def isPalindrome(self, s: str) -> bool:
        validChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        n = len(s) - 1
        i = 0
        for m in range(int((n + 1)/2)):
            while validChars.count(s[i]) < 1:
                if caps.count(s[i]) > 0: 
                    s = s[:i] + validChars[caps.index(s[i])] + s[i + 1:]
                    break
                # Skip invalid letter
                else: i += 1
                if len(s) < 1 or i >= n: return True 

            while validChars.count(s[n]) < 1:
                if caps.count(s[n]) > 0: 
                    s = s[:n] + validChars[caps.index(s[n])] + s[n + 1:]
                    break
                # Skip invalid letter
                else: n -= 1
                if len(s) < 1 or i >= n: return True 

            if s[n] != s[i]: return False
            n -= 1
            i += 1

        return True
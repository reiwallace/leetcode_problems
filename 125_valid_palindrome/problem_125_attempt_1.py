class Solution:
    #O(n) Complexity
    def isPalindrome(self, s: str) -> bool:
        validChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        backwards = ""
        for char in range(len(s) - 1, -1, -1):
            if validChars.count(s[char]) > 0: backwards = backwards + s[char]
            elif caps.count(s[char]) > 0: backwards = backwards + validChars[caps.index(s[char])]

        forwards = ""
        for char in range(len(backwards) - 1, -1, -1):
            forwards = forwards + backwards[char]

        return backwards == forwards
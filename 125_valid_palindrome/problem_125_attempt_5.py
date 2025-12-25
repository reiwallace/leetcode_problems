class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        for i in range(len(s)):
            if s[i] != s[-i - 1]: return False
        return True
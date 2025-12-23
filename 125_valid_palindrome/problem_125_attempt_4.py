class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = 0
        m = len(s) - 1

        while n < m:
            while not s[n].isalnum() and n < m: n += 1
            while not s[m].isalnum() and n < m: m -= 1

            if s[n].lower() != s[m].lower(): return False

            n += 1
            m -= 1
            
        return True


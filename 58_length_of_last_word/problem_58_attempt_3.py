class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        i = 0
        for n in range(len(s)):
            if s[i] == " ":
                if len(s[:i]) > 0: word = s[:i]
                s = s[i + 1:]
                i = -1
            i += 1
        if len(s) > 0 and s[-1] != " ": word = s
        return len(word)
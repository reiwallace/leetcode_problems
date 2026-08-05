class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * len(text1)
        longest = 0

        for char in text2:
            cur_len = 0
            for i, val in enumerate(dp):
                if val > cur_len:
                    cur_len = val
                elif text1[i] == char:
                    dp[i] = cur_len + 1
                    longest = max(longest, cur_len + 1)
        return longest
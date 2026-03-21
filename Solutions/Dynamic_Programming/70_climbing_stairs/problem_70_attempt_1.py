class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1: return 0
        memo = [None] * (n + 1)
        if n < 2: return 1
        memo[1] = 1
        if n < 3: return 2
        memo[2] = 2
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[-1]
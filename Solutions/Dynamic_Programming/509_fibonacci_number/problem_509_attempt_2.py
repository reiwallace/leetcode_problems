class Solution:
    def fib(self, n: int) -> int:
        if n < 1: return 0
        if n == 1 or n == 2: return 1
        memo = [None] * (n + 1)
        memo[1] = 1
        memo[2] = 1
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[-1]
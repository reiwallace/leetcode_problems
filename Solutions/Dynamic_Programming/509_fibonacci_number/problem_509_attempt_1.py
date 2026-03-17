class Solution:
    def fib(self, n: int) -> int:
        if n < 1: return 0
        memo = [None] * (n + 1)
        def calc_fib(n, memo):
            if memo[n] != None:
                return memo[n]
            elif n == 1 or n == 2:
                result = 1
            else:
                result = calc_fib(n - 1, memo) + calc_fib(n - 2, memo)
            memo[n] = result
            return memo[n]
        
        return calc_fib(n, memo)
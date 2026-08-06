class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        divisor = 1
        while n / divisor >= 1:
            divisor *= 10
            digit = (n % divisor) // (divisor / 10)
            if digit % t == 0:
                return n
            

        return min(n + (t - (n % 10 % t)), n + n % 10)
    
        

        
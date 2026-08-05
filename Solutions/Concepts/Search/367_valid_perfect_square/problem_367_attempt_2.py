import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        low, high = 2, math.ceil(num / 3)
        while low <= high:
            mid = (low + high) // 2
            sqr = mid * mid
            if sqr == num:
                return True
            elif sqr > num:
                high = mid - 1
            else:
                low = mid + 1
        return False
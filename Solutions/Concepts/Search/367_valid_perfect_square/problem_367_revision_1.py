class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        top = num
        bottom = 0
        mid = num // 2
        while top >= bottom:
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num: # If sq is bigger than num lower top
                top = mid - 1
            elif sq < num: # If sq is lower than num raise bottom
                bottom = mid + 1
            mid = bottom + (top - bottom) // 2
        return False
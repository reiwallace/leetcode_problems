class Solution:
    # Time Complexity O(n), Space Complexity O(1)
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        steps = [1, 2]
        low = True

        for i in range(2, n):
            if(low):
                steps[0] = steps[1] + steps[0]
            else:
                steps[1] = steps[1] + steps[0]
            low = not low

        return steps[1] if low else steps[0] 
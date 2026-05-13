class Solution:
    # Time Complexity O(n), Space Complexity O(1)
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        steps = [1, 2]

        for i in range(2, n):
            temp = steps[1]
            steps[1] = steps[1] + steps[0]
            steps[0] = temp

        return steps[1]
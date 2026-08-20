from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])

        pairs = sorted(pairs, reverse=True)

        for pos, spe in pairs:
            stack.append((target - pos) / spe)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        daily = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append(1)
            elif temperatures[i] > temperatures[i - 1]:
                while stack:
                    daily.append(stack.pop())
                stack.append(1)
            else:
                stack.append(stack[-1] + 1)
        
        while stack:
            daily.append(0)
            stack.pop()

        return daily
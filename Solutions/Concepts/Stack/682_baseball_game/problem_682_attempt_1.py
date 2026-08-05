from collections import deque
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()

        for op in operations:
            if op == "+":
                previous1 = stack.pop()
                previous2 = stack.pop()
                stack.append(previous2)
                stack.append(previous1)
                stack.append(previous1 + previous2)
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        total = 0
        while stack:    
            total += stack.pop()

        return total
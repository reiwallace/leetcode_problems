import math
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    stack.append(temp2 - temp1)
                case "/":
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    res = temp2 / temp1
                    if res < 0:
                        stack.append(math.ceil(res))
                    else:
                        stack.append(math.floor(res))
                case _:
                    stack.append(int(token))

        return stack.pop()
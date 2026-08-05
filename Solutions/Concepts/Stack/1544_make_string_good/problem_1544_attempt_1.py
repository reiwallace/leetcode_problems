class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) == 0: stack.append(char)
            elif char != stack[-1] and char.lower() == stack[-1].lower():
                stack.pop()
            else: stack.append(char)
        return "".join(stack)
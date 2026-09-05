class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue

            prev = stack[-1]
            
            if char != prev and char.lower() == prev.lower():
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
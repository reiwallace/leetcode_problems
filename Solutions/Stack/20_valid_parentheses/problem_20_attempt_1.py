class Solution:
    def isValid(self, s: str) -> bool:
        openB = ["(", "[", "{", ")", "]", "}"]
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif openB.index(char) > 2:
                if openB.index(stack[-1]) < 3 and char == openB[openB.index(stack[-1]) + 3]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(char)

        return len(stack) == 0
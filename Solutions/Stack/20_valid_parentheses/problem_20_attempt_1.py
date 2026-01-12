class Solution:
    def isValid(self, s: str) -> bool:
        bracket = ["(", "[", "{", ")", "]", "}"]
        stack = [];
        for char in s:
            if len(stack) == 0:
                stack.append(char)
                print("push")
            elif(char == bracket[bracket.index(stack[-1]) + 3]):
                stack.pop()
                print("pop")
            else: 
                stack.append(char)
            print(stack)

        if len(stack) == 2 and stack[0] == stack[1]:
            return True
        return len(stack) == 0
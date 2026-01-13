class Solution:
    # Time complexity O(n), Space complexity O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(" : ")", "[" : "]", "{" : "}"}
        for char in s:
            if not stack:
                stack.append(char)
            elif stack[-1] in mapping and mapping[stack[-1]] == char:
                stack.pop()
            else:
                stack.append(char)
        return not stack
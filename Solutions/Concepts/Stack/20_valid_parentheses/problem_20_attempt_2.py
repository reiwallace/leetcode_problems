class Solution:
    # Time complexity O(n), Space complexity O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            unicode = ord(char)
            if not stack:
                stack.append(unicode)
            elif unicode - 2 == stack[-1] or unicode - 1 == stack[-1]:
                stack.pop()
            else:
                stack.append(unicode)
        return not stack
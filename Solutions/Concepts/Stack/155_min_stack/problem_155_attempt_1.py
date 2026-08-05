class MinStack:
    def __init__(self):
        self.stack = []
        self.lowest = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.lowest or val <= self.lowest[-1]:
            self.lowest.append(val)
        
    def pop(self) -> None:
        val = self.stack.pop()
        if self.lowest and self.lowest[-1] == val:
            self.lowest.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.lowest[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        self.count = 0
        

    def push(self, x: int) -> None:
        if self.count == 0:
            self.stack.append(x)
            self.minStack.append(x)
            self.count += 1
            return 
        min_ = min(self.minStack[-1], x)
        self.stack.append(x)
        self.minStack.append(min_)
        self.count += 1

    def pop(self) -> None:
        if self.count > 0:
            self.minStack.pop()
            self.stack.pop()
            self.count -= 1
        return
    
    def top(self) -> int:
        if self.count == 0:
            return None
        return self.stack[-1]
        
    def getMin(self) -> int:
        if self.count > 0:
            return self.minStack[-1]
        return None
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack:

    def __init__(self):
        self.MinStack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.MinStack.append(val)

        if len(self.minimum) == 0:
            self.minimum.append(val)
        elif len(self.minimum) != 0:
                current_minimum = min(val, self.minimum[-1])
                self.minimum.append(current_minimum)
        else:
            self.minimum.append(val)

    def pop(self) -> None:
        self.MinStack.pop()
        self.minimum.pop()
    
    def top(self) -> int:
       return self.MinStack[-1]
        
    def getMin(self) -> int:
        return self.minimum[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack(object):

    def __init__(self):
        self.Stack=[]
        self.MinStack = []

    def push(self, val):
        self.Stack.append(val)
        val=min(val, self.MinStack[-1] if self.MinStack else val)
        self.MinStack.append(val)

    def pop(self):
        self.Stack.pop()
        self.MinStack.pop()

    def top(self):
        return self.Stack[-1]
        

    def getMin(self):
        return self.MinStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
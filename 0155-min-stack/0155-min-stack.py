class MinStack:
    '''
    
    [ -2, 0, -3 ]
    
    [(-2, 0), (0, 1), (3, 2)]
    
    [ 4, 2, 3 ]
    
    ['', '', '']
    
    sum = 9
    '''

    def __init__(self):
        self.stack = [] # [ -2, 0, -4 ]
        self.min_stack = [] # [ -2, -2, -4 ]


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]) if len(self.min_stack) else val )

    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack):
            return self.min_stack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
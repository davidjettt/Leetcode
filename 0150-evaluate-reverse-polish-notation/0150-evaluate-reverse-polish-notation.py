class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init stack
        # loop through tokens
        # keep adding to stack until reach operator
        # when reach operator, pop off two values of stack
        # compute result of two values with operator
        # put back into stack
        # continue loop until reach the end 
        # final result should be inside stack

        stack = []
        for c in tokens:
            if c == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(b + a)
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif c =='/':
                a, b = stack.pop(), stack.pop()
                stack.append(math.trunc(b / a))
            else:
                stack.append(int(c))
        
                
        return stack[0]
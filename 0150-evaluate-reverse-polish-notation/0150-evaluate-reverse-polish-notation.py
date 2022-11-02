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
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        
        # for i in range(len(tokens)):
        #     if tokens[i].isnumeric():
        #         stack.append(int(tokens[i]))
        #     else:
        #         # v2 = stack.pop()
        #         # v1 = None
        #         # if len(stack) == 0:
        #         #     v1 = 0
        #         # else:
        #         #     v1 = stack.pop()
        #         # print(stack)
        #         v2 = stack.pop()
        #         v1 = stack.pop()
        #         if tokens[i] == '+':
        #             # computation = v1 + v2
        #             stack.append(v1 + v2)
        #         elif tokens[i] == '-':
        #             stack.append(v1 - v2)
        #         elif tokens[i] == '*':
        #             stack.append(v1 * v2)
        #         else:
        #             # stack.append(int(v1 / v2))
        #             stack.append(int(float(v1) / v2))
                
        return stack[0]
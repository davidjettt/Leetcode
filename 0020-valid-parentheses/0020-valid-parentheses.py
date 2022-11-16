class Solution:
    def isValid(self, s: str) -> bool:
        
        
        # init a stack
        # create the hashmap
        
        # iterate through the string
            # if the character is in the hashmap
                # pop off from the stack
                #  check the popped off character to see if it is the right pair (use hashmap to check)
                # if not a matching pair return False
            
            # else
                # add character into the stack
                
                
        # if length of stack is > 0
            # return true
        # else return false
          
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = [] 
        
        for char in s:
            if char in pairs and len(stack):
                ele = stack.pop()
                
                if ele != pairs[char]:
                    return False
                
                    
            else:
                stack.append(char)
        
        return True if not len(stack) else False
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Time O(n)
        # Space O(n)
        
#         stack = []
        
#         open_to_close = {
#             ')': '(',
#             ']': '[',
#             '}': '{'
#         }

#         for char in s:
#             if char in open_to_close:
#                 if stack and stack[-1] == open_to_close[char]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(char)
                
#         if len(stack):
#             return False
                
#         return True
        
        
#         chars = {
#             ')': '(',
#             ']': '[',
#             '}': '{'
#         }

#         stack = []


#         for char in s:
#             if char in chars:
#                 if stack and stack[-1] == chars[char]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(char)


#         if len(stack):
#             return False

#         return True
    
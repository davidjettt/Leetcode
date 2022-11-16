class Solution:
    def isValid(self, s: str) -> bool:
        # Time O(n) n is the size input s
        # Space O(n)
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
        
        
    
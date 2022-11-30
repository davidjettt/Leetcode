class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        {
            'a': 3,
            'b': 4,
            'c': 5
        }
        
        { b,c } 
        res = 1 
        a b c a b c b b
                  l r 
         
          
    
    
        iterate through string using left and right pointers
        
            check if s[r] is in set
                if true, then move left pointer until s[l] == s[r] (plus 1)
                if false, add to set and compute and compare substring size with result
                
        
        return res
        
        Time O(n) where n is the length of the string
        Space O(n) where n is the size of the set
        '''
        res = 0
        chars = set()
        l = 0

        for r in range(len(s)):
            if s[r] in chars:
                while s[l] != s[r] and l < r:
                    chars.remove(s[l])  
                    l += 1
                
                l += 1
            else:
                chars.add(s[r])
                res = max(res, r - l + 1) 
                
        return res
        
        
        # need to find length of longest substring without repeating characters in the answer
    
        # a b c a b c b b
        # l     r
        
        
#         chars = set()
#         res = 0
        
#         l = 0
#         for r in range(len(s)):
#             while s[r] in chars:
#                 chars.remove(s[l])
#                 l += 1
#             chars.add(s[r])
                
#             res = max(res, r - l + 1)
            
#         return res
    
    
#         l, r = 0, 0
#         res = 0
#         seen = set()
        
#         while l < len(s) and r < len(s):
#             if s[r] not in seen:
#                 seen.add(s[r])
#                 res = max(res, r - l + 1)
#                 r += 1
#             else:
#                 seen.remove(s[l])
#                 l += 1
#         return res
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
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
            
        # return res
    
    
        l, r = 0, 0
        res = 0
        seen = set()
        
        while l < len(s) and r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                res = max(res, r - l)
            else:
                seen.remove(s[l])
                l += 1
        return res
        
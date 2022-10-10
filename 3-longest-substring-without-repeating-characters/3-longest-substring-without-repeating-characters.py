class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # need to find length of longest substring without repeating characters in the answer
    
        # a b c a b c b b
        # l     r

# max length is distance + 1 btwn left and right pointers  without repeating characters (r - l) + 1
# iterate through string every time come accross c that is not repeating, count++ and add c to visited 
# keep moving right pointer until come across c that is repeating
# then need to set res to count if count > res, reset count, reset visited, and move left pointer plus 1
# then do the same thing
        
#         pwwkew
#         lr
        
        
#         d a v d f 
#           l   r

  # a d v d f z y
  # l   r  
        
#     b b b b b
    
#     l r
        
        chars = set()
        res = 0
        
        l = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
                
            res = max(res, r - l + 1)
            
        return res
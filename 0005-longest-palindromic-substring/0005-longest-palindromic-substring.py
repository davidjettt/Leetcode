class Solution:
    def longestPalindrome(self, s: str) -> str:
        """"
        
         b a b a d
           i
         
         {
            c: 1,
            b:
         }
         
         
         c b b d
         l r
          
          
          {
            a: 2,
            n: 2
          }
          
           
         a n n a x y z b
         l     r 
         
         iterate through input string
         for odd l, r pointers point to same letter
         use while loop to check if s[r] == s[l] and check if pointers are in bounds
         compare the length of substring with length of result
         move l, r pointers
         
         for even
         right pointer starts at left plus 1
         
         
        """
        # Time O(n^2)
        # Space O(1)
        res = ''
        res_len = 0
        
        for i in range(len(s)):
            # for odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                
                l -= 1
                r += 1
            
            # for even
            l, r = i, i + 1
            
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1
                    
        return res
            
        
        
        
        
        
        # BRUTE FORCE APPROACH
#         res = 'a'
#         for i in range(len(s)):
#             for j in range(i, len(s) + 1):
#                 # print(s[i:j])
#                 if s[i:j] == s[i:j][::-1]:
#                     if len(s[i:j]) > len(res): 
#                         res = s[i:j]
                        
#         return res
        
        